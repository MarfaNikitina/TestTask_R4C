"""R4C URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from customers import views as customer_views
from orders import views as order_views
from robots import views as robot_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/add_robot', robot_views.RobotApiView.as_view(), name='create_robot'),
    path('api/v1/add_order', order_views.OrderApiView.as_view(), name='create_order'),
    path('api/v1/add_customer', customer_views.CustomerApiView.as_view(), name='create_customer'),
]
