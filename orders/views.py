from rest_framework.generics import CreateAPIView

from orders.models import Order
from orders.serializers import OrderSerializer


class OrderApiView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
