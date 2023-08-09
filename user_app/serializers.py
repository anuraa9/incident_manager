from user_app.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)       # Handled Confirm Password Field
    
    class Meta:
        model = User
        fields = "__all__"
        
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'error': 'password and password2 should be same!'})
        
        
        account = User(email=self.validated_data['email'], user_type=self.validated_data['user_type'], first_name=self.validated_data['first_name'], last_name=self.validated_data.get('last_name',None), address=self.validated_data['address'], country=self.validated_data['country'], state=self.validated_data['state'], city=self.validated_data['city'], pincode=self.validated_data['pincode'], mobile_no=self.validated_data['mobile_no'])
        account.set_password(password)
        account.save()
        
        return account
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'user_type', 'first_name', 'last_name', 'address', 'country', 'state', 'city', 'pincode', 'mobile_no']