from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):

    """Test api view."""

    def get(self, request, format=None):

        """Returns a list of APIView Features."""

        an_apiview = [
             'uses http methods as functions ',
             'it is similar to a traditional django view',
             'gives you the most control over the logic',
             'is mapped manually to URLS'
        ]

        return Response({'message':'hello!', 'an_apiview':  an_apiview})
