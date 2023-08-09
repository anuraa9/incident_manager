from rest_framework.views import APIView
from user_app.serializers import RegistrationSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from user_app.models import User
from geopy.geocoders import Nominatim

'''
This class provides post API to logout a User.
Currenly using TokenAUthentication for authentication purpose.
You can find the postman collection in the root folder of this project.
'''  
class LogoutView(APIView):
    def post(self, request):
        request.auth.delete()
        return Response(status=200)
    
'''
This class provides post API to register a User.
Currenly using TokenAUthentication for authentication purposes.
You can find the postman collection in the home folder of this project.
'''    
class RegistrationView(APIView):
    permission_classes = []
    
    def post(self, request):    
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration successful!'
            data['email'] = account.email
            token, _ = Token.objects.get_or_create(user=account)
            data['token'] = token.key            
        else:
            data = serializer.errors
        
        return Response(data)

'''
This class provides get API to edit a Users basic details.
You can find the postman collection in the root folder of this project.
'''    
class UserEditView(APIView):
   def put(self, request):
       serializer = UserSerializer(request.user, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
'''
This Class takes the pin code as request param and returns the city, state and country
WARNING: This function is not properly tested and is dependent OpenStreetMap Location Data
which may not always be correct!! 
'''
class GetLocationData(APIView):
    permission_classes = []
    
    def get(self, request):
        data = {'city':'', 'country':''}
        try:
            pincode = request.query_params.get('pincode')
            if pincode:
                geolocator = Nominatim(user_agent="geoapiExercises")
                location = geolocator.geocode(pincode)
                data['city'] = location.address.split(',')[-4].strip()
                data['state'] = location.address.split(',')[-3].strip()
                data['country'] = location.address.split(',')[-1].strip()
        except:
            pass
        return Response(data)