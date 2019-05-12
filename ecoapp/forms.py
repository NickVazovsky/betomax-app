# -*- coding utf-8 -*-
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Логин"
        self.fields['password1'].label = "Пароль"
        self.fields['password2'].label = "Повторите свой пароль"
        self.fields['email'].label = "Email"
        self.fields['first_name'].label = "Имя"
        self.fields['last_name'].label = "Фамилия"

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserProfileSignupForm(forms.ModelForm):
    info = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'Молод и горяч', }),
        required=False, label=u'Пара слов о себе'
    )
    avatar = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'ask-signup-avatar-input', }),
        required=False, label=u'Аватар'
    )

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar is None:
            raise forms.ValidationError(u'Добавьте картинку')
        if 'image' not in avatar.content_type:
            raise forms.ValidationError(u'Неверный формат картинки')
        return avatar

    class Meta:
        model = UserProfile
        fields = ('info', 'avatar')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))


class OrderForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField(required=False)
    phone = forms.CharField()
    buying_type = forms.ChoiceField(widget=forms.Select(), choices=([('self', 'Самовывоз'), ('delivery', 'Доставка')]))
    date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now())
    address = forms.CharField(required=False)
    comments = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Ваше имя:"
        self.fields['last_name'].label = "Ваша Фамилия:"
        self.fields['phone'].label = "Контактный телефон:"
        self.fields['phone'].help_text = "Пожалуйста указывайте реальный номер телефона чтобы мы могли с вами связаться"
        self.fields['buying_type'].label = "Способ получения"
        self.fields['address'].label = "Адресс доставки:"
        self.fields['address'].help_text = "Обязательно укажите город!"
        self.fields['comments'].label = "Комментарий к заказу:"
        self.fields['date'].label = "Дата доставки:"
        self.fields['date'].help_text = "Доставка производится на следующй день после заказа"


class RentaCarForm(forms.Form):
    fio_renta = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Василий Васильевич Березкин'}))
    phone_renta = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '+99897 988-99-99', 'type': 'text'}))

    def __init__(self, *args, **kwargs):
        super(RentaCarForm, self).__init__(*args, **kwargs)
        self.fields['fio_renta'].label = "ФИО"
        self.fields['phone_renta'].label = "Номер телефона"


class BetonOrdersForm(forms.Form):
    fio_beton = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Василий Васильевич Березкин'}))
    phone_beton = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '+99897 988-99-99'}))

    def __init__(self, *args, **kwargs):
        super(BetonOrdersForm, self).__init__(*args, **kwargs)
        self.fields['fio_beton'].label = "ФИО"
        self.fields['phone_beton'].label = "Номер телефона"


class PersonalOrderForm(forms.Form):
    fio_personal = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Василий Васильевич Березкин'}))
    phone_personal = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '+99897 988-99-99'}))
    image_personal = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(PersonalOrderForm, self).__init__(*args, **kwargs)
        self.fields['fio_personal'].label = "ФИО"
        self.fields['phone_personal'].label = "Номер телефона"
        self.fields['image_personal'].label = "Эскиз вашего проекта"
        self.fields['image_personal'].help_text = "Загружать можно файлы не превышающие 15мб"


class ProductWholesaleForm(forms.Form):
    fio_wholesale = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Василий Васильевич Березкин'}))
    phone_wholesale = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '+99897 988-99-99', 'type': 'text'}))

    def __init__(self, *args, **kwargs):
        super(ProductWholesaleForm, self).__init__(*args, **kwargs)
        self.fields['fio_wholesale'].label = "ФИО"
        self.fields['phone_wholesale'].label = "Номер телефона"


class ExcursionForm(forms.Form):
    name_university = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Betomax_university'}))
    fio_excursion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Василий Васильевич Березкин'}))
    number_students = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '15'}))
    phone_excursion = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '+99897 988-99-99', 'type': 'text'}))

    def __init__(self, *args, **kwargs):
        super(ExcursionForm, self).__init__(*args, **kwargs)
        self.fields['name_university'].label = "Название уебного заведения"
        self.fields['fio_excursion'].label = "ФИО Куратора"
        self.fields['number_students'].label = "Кол-во студентов"
        self.fields['phone_excursion'].label = "Номер телефона"


class ContactsForm(forms.Form):
    fio_contacts = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ФИО',
                                                                 'class': 'form-control'}))
    phone_contacts = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Номер телефона',
                                                                   'class': 'form-control'}))
    questions_contacts = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ваш Вопрос ....',
                                                                      'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(ContactsForm, self).__init__(*args, **kwargs)
        self.fields['fio_contacts'].label = ""
        self.fields['phone_contacts'].label = ""
        self.fields['questions_contacts'].label = ""


class CommentsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ФИО',
                                                         'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email',
                                                          'class': 'form-control'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ваш комментарий',
                                                           'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['email'].label = ""
        self.fields['comment'].label = ""


class FeedbacksForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ФИО',
                                                         'class': 'input_footer'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Номер телефона',
                                                          'class': 'input_footer'}))


class UserUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Имя"
        self.fields['last_name'].label = "Фамилия"
        self.fields['email'].label = "Email"

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class AvatartUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AvatartUpdateForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].label = "Фото профиля"
        self.fields['phone'].label = "Номер телефона"

    class Meta:
        model = UserProfile
        fields = ['avatar', 'phone']
