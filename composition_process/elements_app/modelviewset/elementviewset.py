import json

from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from elements_app.models import Element
from elements_app.modelviewset.mixins import ElementSerializer


class ElementViewSet(ModelViewSet):
    serializer_class = ElementSerializer
    queryset = Element.objects.all()
    model = Element
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            data = request.body
            if data:
                json_data = json.loads(data)
                if json_data.get("name"):
                    Element.objects.create(name=json_data.get("name"))
                    return HttpResponse(
                        json.dumps(
                            {f"success": f"element created: {json_data.get('name')}"}
                        ),
                        content_type="application/json",
                    )
                else:
                    return HttpResponse(
                        json.dumps({"error": "required field is name"}),
                        content_type="application/json",
                    )
        except Exception as e:
            return HttpResponse(
                json.dumps({"error": str(e)}), content_type="application/json"
            )
