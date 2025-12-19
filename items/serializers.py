from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    below_reorder = serializers.ReadOnlyField(source='is_below_reorder')

    class Meta:
        model = Item
        fields = '__all__'

    # Quantity validation
    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative")
        return value
