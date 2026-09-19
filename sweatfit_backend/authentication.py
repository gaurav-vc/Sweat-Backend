from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try:
            return super().authenticate(request)
        except (InvalidToken, AuthenticationFailed):
            # If the token is expired or invalid, treat the user as an AnonymousUser
            # rather than failing the entire request immediately.
            # This allows public endpoints (like GET /api/cms/site-content/) to still succeed
            # because their view-level permissions (IsAdminOrReadOnly) allow AnonymousUsers for safe methods.
            return None
