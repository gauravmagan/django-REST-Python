from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly



from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloApiView(APIView):

    """Test api view."""

    serializer_class = serializers.HelloSerializer




    def get(self, request, format=None):

        """Returns a list of APIView Features."""

        an_apiview = [
             'uses http methods as functions ',
             'it is similar to a traditional django view',
             'gives you the most control over the logic',
             'is mapped manually to URLS'
        ]

        return Response({'message':'hello!', 'an_apiview':  an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():

            name = serializer.data.get('name')
            message = 'Hello {0}' .format(name)

            return Response({'message' : message})

        else:

            return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)

    def put (self, request, pk=None):

         """Handles updating an object"""

         return Response ({'method': 'put'})

    def patch(self, request, pk=None):

         """Patch requests, only updates fields provided in the request."""

         return Response ({'method': 'patch'})

    def delete(self, request, pk=None):

          """ deletes an object."""

          return Response ({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):

    """Test API ViewSet."""

    serializer_class = serializers.HelloSerializer

    def list(self,request):

        """ Returns a Hello Message """

        a_viewset = [
            'Uses action (lists, create, retrieve, update, partial_update)',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request):

        """create a new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        def retrieve(self, request, pk=None):
         """Handles getting an object by its ID."""

         return Response({'http_method': 'GET'})

    def update(self, request, pk=None):

         """ handles updating an object"""

         return Response({'http_method': 'PUT'})

    def partial_update(self,request, pk=None):

        """handles partially updating the object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self,request, pk=None):

        """Handles removing an object."""

        return Response ({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):

    """handles creating updating reading and updating profiles"""

    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):

    """ Checks email and password and Returns an auth token """

    serializer_class = AuthTokenSerializer

    def create(self,request):

        """use the obtainauthtoken APIVIEW to validate and create a token """

        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles creating , reading and updating profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):

        """ Sets the user profile to the logged user."""
        serializer.save(user_profile=self.request.user)
