from rest_framework import serializers
from .models import *


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        lookup_field = 'id'
        exclude = ()
