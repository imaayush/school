
from rest_framework import serializers
from class_room.models import User, Subject, Class

class UserRegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'user_type', "parent", "password")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'user_type', "parent")


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('id', 'name', 'teacher', 'classes')


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = ('id', 'name')