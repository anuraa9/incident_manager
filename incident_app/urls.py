from django.urls import path
from incident_app.views import IncidentListView, IncidentDetailView, IncidentCreateView
urlpatterns = [
    path('list/', IncidentListView.as_view(), name='incident-list'),
    path('create/', IncidentCreateView.as_view(), name='incident-create'),
    path('<int:pk>/', IncidentDetailView.as_view(), name='incident-detail'),
    path('list/search/', IncidentListView.as_view(), name='incident-search'),
] 