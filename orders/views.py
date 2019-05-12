from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import OrderCreated
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from .models import Order


def AdminOrderPDF(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=order_{}.pdf'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + '/css/bootstrap.min.css',)])
    return response


def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            OrderCreated.delay(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
            # return render(request, 'bill_page.html', {'order': order})

    form = OrderCreateForm()
    return render(request, 'checkout.html', {'cart': cart, 'form': form})
