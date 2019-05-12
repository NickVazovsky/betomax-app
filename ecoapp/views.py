from django.shortcuts import render, get_object_or_404
from .models import Category, Product, RentaCar, OrderBeton, PersonalOrder, ProductsWholesale, Excursion, Contacts, \
    Comments, Feedbacks, UserProfile
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.views import login as original_login
from decimal import Decimal
from .forms import (RegisterForm, RentaCarForm, BetonOrdersForm,
                    PersonalOrderForm, ProductWholesaleForm, ExcursionForm,
                    ContactsForm, CommentsForm, FeedbacksForm, UserProfileSignupForm,
                    UserUpdateForm, AvatartUpdateForm)
from cart.forms import CartAddProductForm
from .serializers import ProductSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, mixins
from django.db import transaction
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def personal_cabinet(request):
    user = User.objects.filter(username=request.user)
    user_profile = UserProfile.objects.filter(user=request.user)
    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        user_update_avatar = AvatartUpdateForm(request.POST, instance=request.user.userprofile)
        change_password = PasswordChangeForm(request.user, request.POST)
        if user_update_form.is_valid() and user_update_avatar.is_valid():
            user_update_form.save()
            user_update_avatar.save()
            messages.success(request, f'Ваш профиль успешно обновлен')
        else:
            messages.error(request, f'Пожалуйста исправьте ошибки')
        if change_password.is_valid():
            user = change_password.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, f'Ваш пароль успешно изменен')
        else:
            messages.error(request, f'Исправьте ошибки')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        user_update_avatar = AvatartUpdateForm(instance=request.user.userprofile)
        change_password = PasswordChangeForm(request.user)
    return render(request, 'personal_cabinet.html', {'context': user, 'avatar': user_profile,
                                                     'update_user_form': user_update_form,
                                                     'update_avatar': user_update_avatar,
                                                     'change_password': change_password})


def map_view(request):
    return render(request, 'maps.html')


def feedbacks(request):
    if request.method == "POST":
        feedback_form = FeedbacksForm(request.POST)
        if feedback_form.is_valid():
            name = feedback_form.cleaned_data.get("name")
            phone = feedback_form.cleaned_data.get("phone")
            feed = Feedbacks(name=name, phone=phone)
            feed.save()
            return HttpResponseRedirect('/')
    else:
        feedback_form = FeedbacksForm()
    return HttpResponseRedirect('/')


def base_view(request):
    if request.method == 'POST':
        renta_form = RentaCarForm(request.POST)
        beton_form = BetonOrdersForm(request.POST)
        personal_form = PersonalOrderForm(request.POST, request.FILES)
        wholesales_form = ProductWholesaleForm(request.POST)
        excursion_form = ExcursionForm(request.POST)
        if renta_form.is_valid():
            fio_renta = renta_form.cleaned_data.get('fio_renta')
            phone_renta = renta_form.cleaned_data.get('phone_renta')
            rents = RentaCar(fio_renta=fio_renta, phone_renta=phone_renta)
            rents.save()
        if beton_form.is_valid():
            fio_beton = beton_form.cleaned_data.get('fio_beton')
            phone_beton = beton_form.cleaned_data.get('phone_beton')
            betons = OrderBeton(fio_beton=fio_beton, phone_beton=phone_beton)
            betons.save()
        if personal_form.is_valid():
            fio_personal = personal_form.cleaned_data.get('fio_personal')
            phone_personal = personal_form.cleaned_data.get('phone_personal')
            image_personal = personal_form.cleaned_data.get('image_personal')
            personal_order = PersonalOrder(fio_personal=fio_personal, phone_personal=phone_personal,
                                           image=image_personal)
            personal_order.save()
        if wholesales_form.is_valid():
            fio_wholesale = wholesales_form.cleaned_data.get('fio_wholesale')
            phone_wholesale = wholesales_form.cleaned_data.get('phone_wholesale')
            wholesales = ProductsWholesale(fio_wholesales=fio_wholesale, phone_wholesales=phone_wholesale)
            wholesales.save()
        if excursion_form.is_valid():
            name_university = excursion_form.cleaned_data.get('name_university')
            fio_excursion = excursion_form.cleaned_data.get('fio_excursion')
            number_students = excursion_form.cleaned_data.get('number_students')
            phone_excursion = excursion_form.cleaned_data.get('phone_excursion')
            excursion = Excursion(name_university=name_university, fio_excursion=fio_excursion,
                                  number_students=number_students, phone_excursion=phone_excursion)
            excursion.save()
    else:
        renta_form = RentaCarForm()
        beton_form = BetonOrdersForm()
        personal_form = PersonalOrderForm()
        wholesales_form = ProductWholesaleForm()
        excursion_form = ExcursionForm()
    return render(request, 'base.html', {'renta_form': renta_form, 'beton_form': beton_form,
                                         'personal_form': personal_form, 'wholesales_form': wholesales_form,
                                         'excursion_form': excursion_form})


# Страница с товарами
def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shops.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    com = Comments.objects.filter(product=product)
    category = Category.objects.all()
    products = Product.objects.filter(available=True)
    prod = products.filter(category=category)[:5]

    if request.method == "POST":
        comments_form = CommentsForm(request.POST)
        if comments_form.is_valid():
            name = comments_form.cleaned_data.get('name')
            email = comments_form.cleaned_data.get('email')
            comment = comments_form.cleaned_data.get('comment')
            com_save = Comments(product=product, name=name, email=email, comment=comment)
            com_save.save()
    else:
        comments_form = CommentsForm()
    return render(request, 'product.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'comments_form': comments_form, 'coments': com,
                   'prod': prod})


def about_view(request):
    return render(request, 'about_us.html')


def contact_view(request):
    if request.method == "POST":
        contact_form = ContactsForm(request.POST)
        if contact_form.is_valid():
            fio_contact = contact_form.cleaned_data.get('fio_contacts')
            phone_contacts = contact_form.cleaned_data.get('phone_contacts')
            questions_contacts = contact_form.cleaned_data.get('questions_contacts')
            contact = Contacts(fio_contacts=fio_contact, phone_contacts=phone_contacts,
                               questions_contacts=questions_contacts)
            contact.save()
    else:
        contact_form = ContactsForm()
    return render(request, 'contact_us.html', {'contact_form': contact_form})


def transport_view(request):
    return render(request, 'transport.html')


def change_item_qty(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    qty = request.GET.get('qty')
    item_id = request.GET.get('item_id')
    cart_item = CartItem.objects.get(id=int(item_id))
    cart_item.qty = int(qty)
    cart_item.item_total = int(qty) * Decimal(cart_item.product.price)
    cart_item.save()
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return JsonResponse({
        'cart_total': cart.items.count(),
        'item_total': cart_item.item_total,
        'cart_total_price': cart.cart_total,
    })


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        user_profile_signup_form = UserProfileSignupForm(request.POST, request.FILES)
        if form.is_valid() and user_profile_signup_form.is_valid():
            with transaction.atomic():
                user = form.save()
                user_profile = user_profile_signup_form.save(commit=False)
                user_profile.user = user
                user_profile.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Ваша учетная запись создана! Ваш логин:{username}!')
        else:
            messages.error(request, f'Исправьте ошибки')
    else:
        form = RegisterForm()
        user_profile_signup_form = UserProfileSignupForm()
    return render(request, 'register.html', {'form': form, 'avatar_form': user_profile_signup_form})


def login(request):
    u"""
    Вызывает соответствующее представление Django, анализирует результат.
    В случае ошибки генерирует сообщение и возвращает пользователя на прежнюю страницу.
    """
    response = original_login(request)
    if isinstance(response, HttpResponseRedirect):
        return response
    else:
        messages.error(request, f'Your credentials are wrong. Sorry.')
        return HttpResponseRedirect('/')


class ProductsApiView(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializers
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
