from django_filters import FilterSet
from .models import *


class MachineFilter(FilterSet):
    class Meta:
        model = Machine
        fields = {
            'machine_model': ['exact'],
            'machine_factory_number': ['exact'],
            'engine_model': ['exact'],
            'transmission_model': ['exact'],
            'drive_axle_model': ['exact'],
            'steering_axle_model': ['exact'],
            'client': ['exact'],
            'service_company': ['exact'],
        }


class MaintenanceFilter(FilterSet):
    class Meta:
        model = Maintenance
        fields = {
            'maintenance_type': ['exact'],
            'maintenance_machine__machine_factory_number': ['exact'],
            'maintenance_service_company': ['exact'],
        }