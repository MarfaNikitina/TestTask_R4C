from rest_framework.generics import CreateAPIView
from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerApiView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
