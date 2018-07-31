
from rest_framework import serializers
from class_room.models import User, Subject, Class


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, max_length=50)
    user_class = serializers.PrimaryKeyRelatedField(required=False, queryset=Class.objects.all())
    parents = serializers.PrimaryKeyRelatedField(required=False, many=True,  queryset=User.objects.all(), default=[])

    def create(self, validated_data):
        parents = validated_data.pop("parents")
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        if parents:
            user.parents = parents
        user.save()
        validated_data.pop("password")
        validated_data["parents"] = parents
        validated_data["id"] = user.id
        return validated_data

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'user_type', 'parents', 'password', 'user_class')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'user_type', 'parents', 'user_class')


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'user_type')


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = ('id', 'name')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('id', 'name', 'teachers', 'classes')


class ClassSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name', 'teachers')


class ClassDetailsSerializer(serializers.ModelSerializer):
    subjects = ClassSubjectSerializer(many=True)

    class Meta:
        model = Class
        fields = ('id', 'name', 'subjects')


class UserDetailSerializer(serializers.ModelSerializer):
    user_class = ClassDetailsSerializer(many=False)
    parents = ParentSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'user_type', "parents", "user_class")


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password')