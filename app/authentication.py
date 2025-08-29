from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from django.conf import settings
import base64

class GlobalCredentialsAuthentication(BaseAuthentication):

    def authenticate(self, request):
        
        header_auth = request.headers.get('Authorization')

        if not header_auth or not header_auth.startswith('Basic '):

            return None
        
        postman_token = header_auth.split()[1]  # Token was encrypted

        # Token decryption

        try:

            postman_token_decrypted = base64.b64decode(postman_token).decode('utf-8')

        except UnicodeDecodeError:

            postman_token_decrypted = base64.b64decode(postman_token).decode('latin-1')

        # decrypted username and password

        user_name, password = postman_token_decrypted.split(':')

        if user_name != settings.CREDENTIALS.get('username') or password != password == settings.CREDENTIALS.get('password'):

            raise AuthenticationFailed(('Invalid username/password.'))

        user,a=User.objects.get_or_create(username = settings.CREDENTIALS.get('username'), defaults = {'is_superuser' : True})

        return(user,None)