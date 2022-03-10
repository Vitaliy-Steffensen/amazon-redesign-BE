from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from rest_framework import viewsets




#UserLoginViewSet
class UserLoginViewSet(viewsets.ViewSet):
    # permission_classes = [permissions.AllowAny]

    def create(self, request):
        try:
            username = request.data["username"]
            password = request.data["password"]


            if not username or not password:
                return Response({"error":"Please fill all fields"}, status=status.HTTP_400_BAD_REQUEST)
            
            check_user = User.objects.filter(username=username).exists()
            if check_user == False:
                return Response({"error":"Email does not exsist"}, status=status.HTTP_404_NOT_FOUND)

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=request.user)
                data = {
                    'token': token.key,
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'email': request.user.email,
                    'date_joined': request.user.date_joined,
                }
                return Response({"success":"Successfull login", "data": data}, status=status.HTTP_200_OK)
            else:
                return Response({"error":"Invalid login credentials"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            dict_response = {"error": True, "message": "Invalid cradentials.", "success": False, "data": {}}
            return Response(dict_response, status=status.HTTP_400_BAD_REQUEST)












            


# class Login(APIView):

#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
        

#         if not username or not password:
#             return Response({"error":"Please fill all fields"}, status=status.HTTP_400_BAD_REQUEST)
        
#         check_user = User.objects.filter(username=username).exists()
#         if check_user == False:
#             return Response({"error":"Email does not exsist"}, status=status.HTTP_404_NOT_FOUND)

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             token, created = Token.objects.get_or_create(user=request.user)
#             data = {
#                 'token': token.key,
#                 'first_name': request.user.first_name,
#                 'last_name': request.user.last_name,
#                 'email': request.user.email,
#                 'date_joined': request.user.date_joined,
#             }
#             return Response({"success":"Successfull login", "data": data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error":"Invalid login credentials"}, status=status.HTTP_400_BAD_REQUEST)


# class Register(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
        




""" class UserInformation(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication,)
 """




""" class CreateTokenView(APIView):

    def get(self, request):
        user = Token.objects.get(key=request.data.get('token')).user
        return Response({'email': user.email})
        #response = super(CreateTokenView, self).post(request, *args, **kwargs)
        #token = Token.objects.get(key=response.data['token'])
        
        #user_email = request.data.get('email', None)
        #user = User.objects.get(email=user_email)
        return Response({'email': user.email})

# class CreateTokenView(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         user = Token.objects.get(key=request.data.get('token')).user
#         #response = super(CreateTokenView, self).post(request, *args, **kwargs)
#         #token = Token.objects.get(key=response.data['token'])
        
#         #user_email = request.data.get('email', None)
#         #user = User.objects.get(email=user_email)
#         return Response({'first_name': user.first_name, 'email': user.email})
 """


# class Login():

#     def post(self, request):
#         serializer = LoginUserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         return Response({'first_name': user.first_name, 'email': user.email})



# class Login(ObtainAuthToken):

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data,
#         context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })
    
    
""" def get(self, validated_data):
        user = Token.objects.get(key='token string').user
        return user
 """

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class ExampleView(APIView):

#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)