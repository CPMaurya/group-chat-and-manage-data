from django.contrib.auth.models import User
from rest_framework import serializers


class TokenSerializer(serializers.Serializer):

    client_id = serializers.CharField()
    client_secret = serializers.CharField()
    grant_type = serializers.CharField()
    scope = serializers.CharField()
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)

    class Meta:
        fields = ('client_id', 'client_secret', 'grant_type',
                  'scope', 'username', 'password')


class TokenResponseSerializer(serializers.Serializer):
    """Serialize token response data."""

    access_token = serializers.CharField()
    token_type = serializers.CharField()
    expires_in = serializers.IntegerField()
    scope = serializers.CharField()

    class Meta:
        fields = ('access_token', 'token_type', 'expires_in', 'scope')

