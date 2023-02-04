from rest_framework import serializers
from .models import Robot


class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = ('model', 'version')

    def create(self, validated_data):
        validated_data['serial'] = f'{validated_data["model"]}-{validated_data["version"]}'
        return super().create(validated_data)
