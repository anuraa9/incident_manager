from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from incident_app.models import Incident
from incident_app.serializers import IncidentSerializer
from rest_framework import status

'''
This class provides get API to list the incidents of registered User.
Currenly using TokenAuthentication for authentication purpose.
You can find the postman collection in the root folder of this project.
'''  
class IncidentListView(APIView):
    def get(self, request):
        incident_id = request.query_params.get('incident_id')   # Handled search for incident id
        if incident_id:
            incidents = Incident.objects.filter(incident_user=request.user, incident_id=incident_id)
            serializer = IncidentSerializer(incidents, many=True)
            return Response(serializer.data)
        else:            
            incidents = Incident.objects.filter(incident_user=request.user)
            serializer = IncidentSerializer(incidents, many=True)
            return Response(serializer.data)
    
'''
This class provides post API to create the incidents of respected User.
Currenly using TokenAuthentication for authentication purpose.
You can find the postman collection in the root folder of this project.
'''     
class IncidentCreateView(APIView):   
    def post(self, request):
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(incident_user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    
'''
This class provides get, put & delete API to view, update & delete the incidents of respected User.
Currenly using TokenAuthentication for authentication purpose.
You can find the postman collection in the root folder of this project.
''' 
class IncidentDetailView(APIView):
    def get(self, request, pk):
        try:
            incident = Incident.objects.get(incident_user=request.user, pk=pk)
        except Incident.DoesNotExist:
            return Response({'status': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = IncidentSerializer(incident)
        return Response(serializer.data)
        
    def put(self, request, pk):
        try:
            incident = Incident.objects.get(incident_user=request.user, pk=pk)
        except Incident.DoesNotExist:
            return Response({'status': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = IncidentSerializer(incident, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            incident = Incident.objects.get(incident_user=request.user, pk=pk)
        except Incident.DoesNotExist:
            return Response({'status': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        incident.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)