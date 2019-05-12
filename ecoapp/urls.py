from .views import (base_view, about_view, contact_view,
                    transport_view, login, registration,
                    ProductList, ProductDetail, map_view)
from django.contrib.auth.views import logout
from django.conf import settings

from ecoapp.views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'products', ProductsApiView)

urlpatterns = [

    url(r'^api_shop/', include(router.urls)),
    url(r'^auth_api/', obtain_jwt_token),
    url(r'^feedbacks/', feedbacks, name='feedback'),
    url(r'^personal/', personal_cabinet, name='personal'),
    url(r'^maps/', map_view),
    url(r'^shops/', ProductList, name='shops'),
    url(r'^about_us', about_view, name='about_us'),
    url(r'^contacts', contact_view, name='contact_us'),
    url(r'^transport', transport_view, name='transport'),
    url(r'^register/', registration, name='register'),
    url(r'^auth/login/$', login),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^auth/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', base_view, name='base'),
    url(r'^(?P<category_slug>[-\w]+)/$', ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', ProductDetail, name='ProductDetail'),

]
