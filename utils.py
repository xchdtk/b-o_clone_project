import jwt
import json
from django.http import JsonResponse
from westagram.settings import SECRET

from user.models import Users
from posting.models import Post_register


def login_decorator(func): 
    def wrapper(self, request, *args, **kwargs):
        try:
            token        = request.headers.get("Authorization")
            jwt_user     = jwt.decode(token, SECRET, algorithms="HS256")
            user = Users.objects.get(id = jwt_user["id"])
            request.user = user
        
        except Users.DoesNotExist:
            return return JsonResponse({"message :" : "해당 유저가 없습니다."}, status=401)
            
        return func(self, request, *args, **kwargs)
    return wrapper
