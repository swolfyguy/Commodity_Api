import json

from django.http import HttpResponse, JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from elements_app.models import Commodity, Element, Composition
from elements_app.modelviewset.mixins import SerializeMixin, CommoditySerializer


class CommodityViewSet(ModelViewSet, SerializeMixin):
    serializer_class = CommoditySerializer
    queryset = Commodity.objects.all()
    model = Commodity
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_element_by_id(self, serialized_composition_obj):
        element_list = []
        for composition_ele in json.loads(serialized_composition_obj):
            emp = Element.objects.get(id=composition_ele.get("element_id"))
            json_data = self.serialize(
                [
                    emp,
                ]
            )

            composition_ele.update(
                {
                    "element": {
                        "id": composition_ele.get("element_id"),
                        "name": json.loads(json_data)[0].get("name"),
                    }
                }
            )
            element_list.append(composition_ele)
            del composition_ele["element_id"]
            del composition_ele["commodity_id"]
        return element_list

    def add_unknow_element(self, chemical_composition):
        if chemical_composition:
            percentage = 0
            for chemical in chemical_composition:
                percentage = percentage + chemical.get("percentage", 0)
            if percentage < 100:
                chemical_composition.append(
                    {
                        "element": {"id": 0, "name": "unknown_element"},
                        "percentage": (100 - percentage),
                    }
                )

    def retrieve(self, request, pk):
        try:
            commodity_model = Commodity.objects.get(id=pk)
            composition_model = Composition.objects.filter(commodity_id=commodity_model)
            serialized_composition_obj = self.serialize(composition_model)
        except Commodity.DoesNotExist as e:
            return HttpResponse(
                json.dumps({"error": "Id not found"}), content_type="application/json"
            )
        else:
            json_data = self.serialize(
                [
                    commodity_model,
                ]
            )
            data = json.loads(json_data)[0]
            chemical_composition = self.get_element_by_id(serialized_composition_obj)
            self.add_unknow_element(chemical_composition)
            data.update({"chemical_composition": chemical_composition})
            return JsonResponse(data, content_type="application/json")
