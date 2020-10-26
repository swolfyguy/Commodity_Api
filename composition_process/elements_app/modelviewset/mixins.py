from django.core import serializers
from django.core.serializers import serialize
from rest_framework import serializers
import json
from elements_app.models import Commodity, Composition, Element


class SerializeMixin(object):
    def serialize(self, qs):
        json_data = serialize("json", qs)
        pdict = json.loads(json_data)
        final_list = []
        for obj in pdict:
            final_list.append(obj["fields"])
            json_data = json.dumps(final_list)
        return json_data


class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = "__all__"


class CompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composition
        fields = "__all__"


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = "__all__"
