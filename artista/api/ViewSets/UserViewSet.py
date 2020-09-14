from rest_framework import serializers,viewsets,routers
from register.models import User,Role

from ..Serializers.UserSerializer import UserSerializer,RoleSerializer

# ViewSets define the view behavior.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
