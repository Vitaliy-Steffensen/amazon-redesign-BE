from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from rest_framework.response import Response



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True,
        }}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        Token.objects.create(user=user)
        return user





# class LoginUserSerializer(serializers.Serializer):
#     phone = serializers.CharField()
#     password = serializers.CharField(
#         style={'input_type': 'password'}, trim_whitespace=False)

#     def validate(self, attrs):
#         phone = attrs.get('phone')
#         password = attrs.get('password')

#         if phone and password:
#             if User.objects.filter(phone=phone).exists():
#                 user = authenticate(request=self.context.get('request'),
#                                     phone=phone, password=password)

#             else:
#                 msg = {'detail': 'Phone number is not registered.',
#                        'register': False}
#                 raise serializers.ValidationError(msg)

#             if not user:
#                 msg = {
#                     'detail': 'Unable to log in with provided credentials.', 'register': True}
#                 raise serializers.ValidationError(msg, code='authorization')

#         else:
#             msg = 'Must include "username" and "password".'
#             raise serializers.ValidationError(msg, code='authorization')

#         attrs['user'] = user
#         return attrs