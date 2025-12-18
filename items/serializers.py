from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    needs_reorder = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = '__all__'

    # Validate quantity
    def validate_quantity_available(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative")
        return value

    # Validate item code
    def validate_item_code(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Item code must be at least 3 characters")
        return value

    # needs_reorder field
    def get_needs_reorder(self, obj):
        return obj.needs_reorder()
