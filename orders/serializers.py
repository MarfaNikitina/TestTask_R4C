from rest_framework import serializers
from orders.models import Order
from orders.services import is_robot_in_stock


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('customer', 'robot_serial')

    def create(self, validated_data):
        validated_data['status'] = is_robot_in_stock(validated_data['robot_serial'])
        return super().create(validated_data)
