from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # Для пользователя. Предоставляет базовую информацию

    class Meta:
        model = User
        fields = (
            'pk', 'email', 'username',
        )

    # def get_fio(self, obj):
    #     return obj.first_name + obj.last_name

    # def to_representation(self, obj):
    #     data = super(UserSerializer, self).to_representation(obj)
    #     data['balance'] = 99
    #     data['email'] = 3221
    #     return data

