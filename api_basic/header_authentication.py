from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class ExampleAuthentication(authentication.BaseAuthentication):
    def  authenticate(self, request):
        username= request.META.get('X-REMOTE-USER')
        if not username :
            return  None
        try :
            user=User.objects.get(username=username)
        except Exception:
            raise exceptions
        return  (user,None)
            