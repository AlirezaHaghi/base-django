from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["POST"])
@permission_classes([AllowAny])
def api_login(request):
    """
    API Login endpoint that returns a token for authentication.
    Does not require CSRF token.
    """
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "message": "Login successful",
            },
            status=status.HTTP_200_OK,
        )
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
def api_logout(request):
    """
    API Logout endpoint that deletes the user's token.
    """
    try:
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
    except Token.DoesNotExist:
        return Response({"error": "Token not found"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def api_user_info(request):
    """
    Get current user information.
    """
    return Response(
        {
            "user_id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "is_staff": request.user.is_staff,
            "is_superuser": request.user.is_superuser,
        },
        status=status.HTTP_200_OK,
    )
