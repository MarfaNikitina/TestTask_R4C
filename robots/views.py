from rest_framework.generics import CreateAPIView
from robots.serializers import RobotSerializer


class RobotApiView(CreateAPIView):
    serializer_class = RobotSerializer
