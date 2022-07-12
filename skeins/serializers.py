from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from skeins.models import Colour, Component, Fibre, Manufacturer, Skein


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["id", "name", "website"]


class ColourSerializer(serializers.ModelSerializer):
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all())
    class Meta:
        model = Colour
        fields = ["id", "manufacturer", "name", "symbol"]

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, UniqueTogetherValidator):
                self.validators.remove(validator)
        super().run_validators(value)
    

class FibreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fibre
        fields = ["id", "name"]
        
class ComponentSerializer(serializers.ModelSerializer):
    fibre = serializers.PrimaryKeyRelatedField(queryset=Fibre.objects.all())
    class Meta:
        model = Component
        fields = ["id", "fibre", "percent"]


class SkeinSerializer(serializers.ModelSerializer):
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all())
    # colours = serializers.PrimaryKeyRelatedField(queryset=Colour.objects.all(), many=True)
    colours = ColourSerializer(many=True)
    composition = ComponentSerializer(many=True)
    # composition = serializers.PrimaryKeyRelatedField(queryset=Fibre.objects.all(), many=True)
    
    class Meta:
        model = Skein
        fields = [
            "id", "form", "manufacturer", "composition", "threads_number", "special_thread", 
            "length", "weight", "colours", "manufacturer_symbol", "prepared", "status", "web_link"
            ]


    def create(self, validated_data):
        components_data = validated_data.pop("composition")
        colours_data = validated_data.pop("colours")
        components = []
        
        
        for component_data in components_data:
            component, _ = Component.objects.get_or_create(**component_data)
          
            components.append(component)
        for colour_data in colours_data:
            # colour, _ = Colour.objects.get_or_create(**colour_data)
            colour = Colour.objects.create(**colour_data)
            colours.append(colour)
            # skein.colours.add(colour)
        colours = [Colour.objects.create(**colour_data) for colour_data in colours_data]
        skein = Skein.objects.create(**validated_data)
        skein.colours.set(colours)
        skein.composition.set(components)
        breakpoint()
        return skein
    
    def to_internal_value(self, data):
        for colour in data["colours"]:
            colour["manufacturer"] = data["manufacturer"]
        return super().to_internal_value(data)

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     breakpoint()
    #     # representation["month"] = representation["month"]["name"]
    #     return representation