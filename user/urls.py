from django.urls import path
from user.views  import SignIn, SignUp

urlpatterns = [
    path('/signup', SignUp.as_view()),
    path('/signin', SignIn.as_view())
]