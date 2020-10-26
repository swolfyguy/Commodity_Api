import json

from django.http import HttpResponse, JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from elements_app.models import Composition, Commodity
from elements_app.modelviewset.mixins import CompositionSerializer


class CompositionViewSet(ModelViewSet):
    serializer_class = CompositionSerializer
    queryset = Composition.objects.all()
    model = Composition
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        body = request.body
        element_composition_payload = json.loads(body)
        element_id = element_composition_payload.get("element_id")
        commodity_id = element_composition_payload.get("commodity_id")

        if not commodity_id or not element_id:
            return JsonResponse(
                {"error": "commodity_id or/and element_id cannot be empty"},
                content_type="application/type",
            )
        try:
            composition_serializer = CompositionSerializer(
                data=element_composition_payload
            )
            commodity_model = Commodity.objects.filter(id=commodity_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, content_type="application/type")

        if commodity_model:
            # Todo update codes need to come here
            composition_model = Composition.objects.filter(
                commodity_id=commodity_id
            ).filter(element_id=element_id)
            if composition_model:
                # serializer = CompositionSerializer(element_data,data=concentration_data,many=True)
                return JsonResponse(
                    {
                        "error": "Api does not support adding existing element to commodity"
                    },
                    content_type="application/type",
                )
        else:
            return JsonResponse(
                {"error": "commodity id not found"}, content_type="application/type"
            )

        return self.update_composition(
            composition_serializer, commodity_id, element_composition_payload
        )

    def update_composition(
        self, composition_serliazer, commodity_id, composition_payload
    ):
        composition_model_lst = Composition.objects.filter(commodity_id=commodity_id)
        element_percentage = 0

        for composition_model in composition_model_lst:
            element_percentage += composition_model.percentage

        if element_percentage + composition_payload["percentage"] <= 100:
            if composition_serliazer.is_valid():
                composition_serliazer.save()
            return JsonResponse(composition_payload, content_type="application/json")
