from django.shortcuts import render
from django.http      import JsonResponse
from django.views     import View

from my_settings      import SECRET, ALGORISM
from user.models      import User


class SignIn(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email  = data['email']
            password = data['password']

            if not email and not password:
                return JsonResponse({"message": "이메일과 비밀번호를 입력해주세요"}, status = 400) 
            if not email:
                return JsonResponse({"message" : "이메일 입력해주세요"})
            if not password:
                return JsonResponse({"message": "패스워드 입력해주세요"}, status = 400) 

            if User.objects.filter(email = email).exists():
                user =  User.objects.get(email = email)

                if bcrypt.checkpw(password.encode('utf-8'),user.password.encode('utf-8')):
                    access_token = jwt.encode({'id' : user.id}, SECRET, ALGORISM)
            
                    token = {
                        'message' : "SUCCESS",
                        "Authorization" : access_token
                    }
                    
                    return JsonResponse(token, status = 201)
                return JsonResponse( {"message" : "잘못된 로그인 시도"}, status = 400)
            
        except KeyError as e:
            return JsonResponse({"message" : e.args[0] + " keyerror"}, status = 400)

        except User.DoesNotExist:
            return JsonResponse({"message": "잘못된 로그인 시도"}, status = 400) 






class SignUp(View):
    def post(self, request):
        data         = json.loads(request.body)
        MAX_PASSWORD = 1000
        MIN_PASSWORD = 10
        try:
            first_name            = data["firstname"]
            last_name             = data['lastname']
            email                 = data["email"]
            password              = data["password"]
            check_password        = data['checkpassword'] 
            receive_communication = data['adagreement'] 

            if not first_name:
                return JsonResponse({"message" :"이름을 입력해주세요"}, status = 400)
            if not last_name:
                return JsonResponse({"message" :"성을 입력해주세요"}, status = 400)
            if not email:
                return JsonResponse({"message" :"이메일를 입력해주세요"}, status = 400)

            email_check   = re.match("\w+\@[a-zA-Z]+\.[a-zA-Z]+", email)   

            if not email_check:
                return JsonResponse({'MESSAGE': 'INVALID_EMAIL'}, status=400)
            if not password:
                return JsonResponse({"message" :"비밀번호를 입력해주세요"}, status = 400)

            if not  len(password) < 10 or len(password) > 1000:
                return JsonResponse({"message" :"비밀번호는 최소 10자, 최대 1000자여야 합니다."}, status = 400)

            if password != check_password:
                return JsonResponse({"message" :"비밀번호 및 확인 비밀번호가 일치하지 않습니다"}, status = 400)

            if User.objects.filter(email = email).exists():
                return JsonResponse({"message" :"회원가입 되어있습니다."}, status = 400)
                
            password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            User.objects.create(
                            first_name            = first_name,
                            last_name             = last_name,
                            email                 = email,
                            password              = password.decode('utf-8'),
                            receive_communication = receive_communication
                            )

            return JsonResponse({"message" :"SUCCESS"}, status = 201)

        except KeyError as e:
            return JsonResponse({"message" : e.args[0] + " keyerror"}, status = 400)