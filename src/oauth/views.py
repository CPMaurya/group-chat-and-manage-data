import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from oauth2_provider.settings import oauth2_settings
from oauth2_provider.views.mixins import OAuthLibMixin
from rest_framework import status

from rest_framework import generics
from rest_framework.response import Response

from .serializers import TokenSerializer, TokenResponseSerializer


class CustomOAuthTokenView(OAuthLibMixin, generics.CreateAPIView):
    """
    View to generate an access token, for a given username.
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = TokenSerializer

    server_class = oauth2_settings.OAUTH2_SERVER_CLASS
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    def create(self, request, *args, **kwargs):
        print("hello")
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # ### TODO: Extract & save uuid part only,
        # ### instead of complete firebase user id.
        username = serializer.validated_data.get('username')
        credentials = {
            'username': username,
            'password': serializer.validated_data.get('password')
        }
        user = authenticate(request, **credentials)
        if user is None:
            response = {'detail': 'Invalid username/password.'}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        url, headers, body, status_code = self.create_token_response(request)
        response_serializer = TokenResponseSerializer(data=body)
        response_serializer.is_valid()
        body = json.loads(body)
        if 'error' in body:
            response = {'detail': 'Invalid Client.'}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        groups = user.groups.values_list('name', flat=True)
        body.update({
            'user_id': user.id,
            'username': user.username,
            'fullname': user.get_full_name(),
            'roles': groups
        })
        return Response(body, status=status_code, headers=headers)
