from django.conf import settings
from orders.models import Order
from robots.models import Robot
from django.core.mail import send_mail

EMAIL_MESSAGE = 'Добрый день! Недавно вы интересовались нашим роботом ' \
                'модели {robot_model}, версии {robot_version}. ' \
                'Этот робот теперь в наличии. ' \
                'Если вам подходит этот вариант - пожалуйста, свяжитесь с нами'

EMAIL_SUBJECT = 'Уведомление о поступлении в наличие'


def send_email_to_customer(robot_serial: str):
    """Function that sends emails for customers."""
    emails = get_waiting_customers_emails(robot_serial)
    message = EMAIL_MESSAGE.format(robot_model=robot_serial[:2], robot_version=robot_serial[3:])
    send_mail(EMAIL_SUBJECT, message, settings.EMAIL_HOST_USER, emails)


def get_waiting_customers_emails(robot_serial: str) -> list[str]:
    """Function that returns list of emails for sending message."""
    waiting_orders = Order.objects.filter(status=False, robot_serial=robot_serial)
    return [order.customer.email for order in waiting_orders]


def is_robot_in_stock(robot_serial: str) -> bool:
    """Function that checks for the presence of a robot."""
    return Robot.objects.filter(serial=robot_serial).exists()
