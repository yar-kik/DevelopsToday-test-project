from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer, LoginSerializer


class RegistrationApiView(APIView):
    """Allow any user access to endpoint"""

    serializer_class = RegistrationSerializer

    def post(self, request: Request) -> Response:
        """Register new user"""
        user = request.data.get("user", {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"user": serializer.data}, status=status.HTTP_201_CREATED
        )


class LoginApiView(APIView):
    serializer_class = LoginSerializer

    def post(self, request: Request) -> Response:
        user = request.data.get("user", {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(
            {"user": serializer.data}, status=status.HTTP_200_OK
        )
