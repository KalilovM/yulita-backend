from rest_framework import viewsets, mixins, permissions
from .models import ClothModel, ClothType, Suit, Size, Textile
from .serializers import CreateClothModelSerializer, ClothModelSerializer, CreateClothTypeSerializer, \
    ClothTypeSerializer, CreateSuitSerializer, SuitSerializer, CreateSizeSerializer, SizeSerializer, \
    CreateTextileSerializer, TextileSerializer


class ClothModelViewSet(viewsets.ModelViewSet):
    """
    Viewset for cloth model
    Allows to create, read, update and delete cloth model
    """
    queryset = ClothModel.objects.all()
    serializer_class = ClothModelSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateClothModelSerializer
        return ClothModelSerializer


class ClothTypeViewSet(viewsets.ModelViewSet):
    """
    Viewset for cloth type
    Allows to create, read, update and delete cloth type
    """
    queryset = ClothType.objects.all()
    serializer_class = ClothTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateClothTypeSerializer
        return ClothTypeSerializer


class SuitViewSet(viewsets.ModelViewSet):
    """
    Viewset for suit
    Allows to create, read, update and delete suit
    """
    queryset = Suit.objects.all()
    serializer_class = SuitSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateSuitSerializer
        return SuitSerializer


class SizeViewSet(viewsets.ModelViewSet):
    """
    Viewset for size
    Allows to create, read, update and delete size
    """
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateSizeSerializer
        return SizeSerializer


class TextileViewSet(viewsets.ModelViewSet):
    """
    Viewset for textile
    Allows to create, read, update and delete textile
    """
    queryset = Textile.objects.all()
    serializer_class = TextileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateTextileSerializer
        return TextileSerializer
