from rest_framework import serializers,viewsets,routers
from register.models import User

from ..Serializers.UserSerializer import UserSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
