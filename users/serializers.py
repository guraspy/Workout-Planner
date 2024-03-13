from rest_framework import serializers
from .models import User

class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'username', 'password', 'birthdate', 'weight']
        extra_kwargs = {
            'password': {'write_only': True}, 
            'birthdate': {'required': False}, 
            'weight': {'required': False},
        }
        
    # Hashing password in database
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'birthdate', 'weight', 'desired_weight']
        extra_kwargs = {
            'birthdate': {'required': False}, 
            'weight': {'required': False}, 
            'desired_weight': {'required': False}
        }