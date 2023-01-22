from rest_framework import serializers
from models import ClothModel, ClothType, Suit, Size, Textile


class CreateClothModelSerializer(serializers.ModelSerializer):
    """
    Serializer for creating cloth model
    """

    class Meta:
        model = ClothModel
        fields = "__all__"


class ClothModelSerializer(serializers.ModelSerializer):
    """
    Serializer for read cloth model
    """

    class Meta:
        model = ClothModel
        fields = "__all__"


class CreateClothTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for creating cloth type
    """

    class Meta:
        model = ClothType
        fields = "__all__"


class ClothTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for read cloth type
    """

    class Meta:
        model = ClothType
        fields = "__all__"


class CreateSuitSerializer(serializers.ModelSerializer):
    """
    Serializer for creating suit
    """

    class Meta:
        model = Suit
        fields = "__all__"


class SuitSerializer(serializers.ModelSerializer):
    """
    Serializer for read suit
    """

    class Meta:
        model = Suit
        fields = "__all__"


class CreateSizeSerializer(serializers.ModelSerializer):
    """
    Serializer for creating size
    """

    class Meta:
        model = Size
        fields = "__all__"


class SizeSerializer(serializers.ModelSerializer):
    """
    Serializer for read size
    """

    class Meta:
        model = Size
        fields = "__all__"


class CreateTextileSerializer(serializers.ModelSerializer):
    """
    Serializer for creating textile
    """

    class Meta:
        model = Textile
        fields = "__all__"


class TextileSerializer(serializers.ModelSerializer):
    """
    Serializer for read textile
    """

    class Meta:
        model = Textile
        fields = "__all__"
