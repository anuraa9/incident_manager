from rest_framework import serializers
from incident_app.models import Incident
from user_app.serializers import UserSerializer

class IncidentSerializer(serializers.ModelSerializer):
    incident_user = UserSerializer(read_only=True)
    class Meta:
        model = Incident
        fields = '__all__'
        read_only_fields = ['incident_id'] 
        
    def update(self, instance, validated_data):
        if instance.status == "Closed":
            raise serializers.ValidationError("Cannot update a closed incident.")
        return super().update(instance, validated_data)