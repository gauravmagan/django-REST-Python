from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from . import serializers

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

    def list(self,request):

        """ Returns a Hello Message """

        a_viewset = [
            'Uses action (lists, create, retrieve, update, partial_update)',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
