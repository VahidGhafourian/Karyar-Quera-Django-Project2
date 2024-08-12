from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'phone',
                  'address',
                  'gender',
                  'age',
                  'description',
                  'first_name',
                  'last_name',
                  'email')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
