from django.db import models
from user_app.models import User
import datetime, random

class Incident(models.Model):
    incident_id = models.CharField(unique=True, max_length=12)
    incident_user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.CharField(max_length=1000)
    PRIORITY_OPTIONS = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    priority = models.CharField(max_length=6, choices=PRIORITY_OPTIONS)
    STATUS_OPTIONS = [
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('In Progress', 'In Progress')
    ]

    status = models.CharField(max_length=11, choices=STATUS_OPTIONS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    '''
    Auto-generate Incident ID and ensure that the format for the Incident
    ID should be the following format- RMG + Random 5-digit number+
    Current year (2023) e.g. RMG345712022
    
    Let it generate a new Random number if the Generated ID is not unique.
    
    WARNING: This function is not reliable if no of incidents are very high.
    '''
    def generate_incident_id(self):
        current_year = datetime.datetime.now().year
        while True:
            random_number = random.randint(10000, 99999)        
            incident_id = 'RMG' + str(random_number) + str(current_year)
            if not Incident.objects.filter(incident_id=incident_id).exists():
                return incident_id

    def save(self, *args, **kwargs):
        if not self.incident_id:
            self.incident_id = self.generate_incident_id()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.incident_id)