from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser

from rest_framework import HTTP_HEADER_ENCODING, authentication, exceptions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            return obj.user == request.user
        except:
            return obj.host == request.user
class APIRequestAuthentication(authentication.BaseAuthentication):
  def authenticate(self, request):
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, str):
      auth = auth.encode(HTTP_HEADER_ENCODING)

    pieces = auth.split()
    if not pieces or pieces[0].lower() != b'token':
      return None

    if len(pieces) == 1:
      msg = _("Invalid token header. No credentials provided.")
      raise exceptions.AuthenticationFailed(msg)
    elif len(pieces) > 2:
      msg = _("Invalid token header."
          "Token string should not contain spaces.")
      raise exceptions.AuthenticationFailed(msg)

    try:
      auth = pieces[1].decode()
    except UnicodeError:
      msg = _("Invalid token header. "
          "Token string should not contain invalid characters.")

    return (AnonymousUser(), auth)
