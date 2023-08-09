from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from user_app.views import RegistrationView, LogoutView, UserEditView, GetLocationData
urlpatterns = [
    path('login/', obtain_auth_token, name='login'),        # Using predefined TokenAuthentication function to create token
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit/', UserEditView.as_view(), name='edit'),
    path('get_location_data/', GetLocationData.as_view(), name='get-location-data')
] 