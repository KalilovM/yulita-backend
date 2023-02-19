from rest_framework import mixins, viewsets, permissions, generics
from apps.user.serializers import UserSerializer
from apps.user.models import User


class CurrentUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
