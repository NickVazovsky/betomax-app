from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def OrderCreated(order_id):
    """
    Отправка сообщений на мыло

    :param order_id:
    :return:
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ с номером {}'.format(order_id)
    message = 'Дорогой, {}, вы успешно сделали заказ.\
                  Номер вашего заказа {}'.format(order.first_name, order.id)
    mail_send = send_mail(subject,message, 'admin@betomax_shop.ru', [order.email])
    return mail_send