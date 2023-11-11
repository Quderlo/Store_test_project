import django.contrib.auth.backends
from django.conf import settings
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # Для пользователя. Предоставляет базовую информацию и баланс

    fio = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'pk', 'email', 'username', 'first_name', 'last_name', 'fio',
        )

    def get_fio(self, obj):
        return obj.first_name + obj.last_name

    def to_representation(self, obj):
        data = super(UserSerializer, self).to_representation(obj)
        data['balance'] = 99
        data['email'] = 3221
        return data
