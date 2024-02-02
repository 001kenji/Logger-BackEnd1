from .models import User
from rest_framework import serializers


class UserSterializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email']

