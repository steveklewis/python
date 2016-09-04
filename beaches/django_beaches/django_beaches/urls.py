from django.conf.urls import include, url
from django.contrib.auth.models import User
from django.contrib import admin

from rest_framework import routers, serializers, viewsets

from beaches_app.models import Beach

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','is_staff')

class BeachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beach
        fields = ('name', 'score')

# ViewSets define the view behavior
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BeachViewSet(viewsets.ModelViewSet):
    queryset = Beach.objects.all()
    serializer_class = BeachSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'beaches', BeachViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_beaches.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
