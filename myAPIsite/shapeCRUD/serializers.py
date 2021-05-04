from rest_framework import serializers
from shapeCRUD.models import Diamond, Rectangle, Square, Triangle
from django.contrib.auth.models import User, Group
import numpy as np


class TriangleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    angle_1 = serializers.IntegerField()
    angle_2 = serializers.IntegerField()
    angle_3 = serializers.IntegerField()
    length_1 = serializers.IntegerField()
    length_2 = serializers.IntegerField()
    length_3 = serializers.IntegerField()


    def create(self, validated_data):
        """
        Create and return a new `Triangle` instance, given the validated data.
        """
        print(validated_data.keys())

        n_1 = np.sin(validated_data['angle_1'])/ validated_data['length_1']
        n_2 = np.sin(validated_data['angle_2']) / validated_data['length_2']
        n_3 = np.sin(validated_data['angle_3']) / validated_data['length_3']

        print(n_1,n_2,n_3)

        if (validated_data['angle_1']+validated_data['angle_2']+validated_data['angle_3'] == 180)&(n_1==n_2==n_3):

            return Triangle.objects.create(**validated_data)
        else:
            return "Triangle not Valid"

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        n_1=np.sin(validated_data.angle_1)/ validated_data.length_1
        n_2=np.sin(validated_data.angle_2) / validated_data.length_2
        n_3=np.sin(validated_data.angle_3) / validated_data.length_3

        if (validated_data.angle_1+validated_data.angle_2+validated_data.angle_3 == 180)&(n_1==n_2==n_3):

            return Triangle.objects.create(**validated_data)
        else:
            return "Triangle not Valid"
        
class RectangleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    length_1 = serializers.IntegerField()
    length_2 = serializers.IntegerField()


    def create(self, validated_data):
        """
        Create and return a new `Rectangle` instance, given the validated data.
        """
        return Rectangle.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        return Rectangle.objects.create(**validated_data)

class SquareSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    length_1 = serializers.IntegerField()


    def create(self, validated_data):
        """
        Create and return a new `Square` instance, given the validated data.
        """
        return Square.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        return Square.objects.create(**validated_data)

class DiamondSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    angle_1 = serializers.IntegerField()
    angle_2 = serializers.IntegerField()
    length_1 = serializers.IntegerField()




    def create(self, validated_data):
        """
        Create and return a new `Diamond` instance, given the validated data.
        """

        if (validated_data['angle_1']+validated_data['angle_2']==180):

            return Diamond.objects.create(**validated_data)
        else:
            return "Diamond not Valid"

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        if (validated_data['angle_1']+validated_data['angle_2']==180):

            return Diamond.objects.create(**validated_data)
        else:
            return "Diamond not Valid"


class UserSerializer(serializers.ModelSerializer):
    squares = serializers.PrimaryKeyRelatedField(many=True, queryset=Square.objects.all())
    triangles = serializers.PrimaryKeyRelatedField(many=True, queryset=Triangle.objects.all())
    diamonds = serializers.PrimaryKeyRelatedField(many=True, queryset=Diamond.objects.all())
    rectangles = serializers.PrimaryKeyRelatedField(many=True, queryset=Rectangle.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'squares','triangles','diamonds','rectangles']

