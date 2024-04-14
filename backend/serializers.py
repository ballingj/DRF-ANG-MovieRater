from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password']
        # hides the password field from get 
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
    # overwrite the  create method to hash the password creation
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']