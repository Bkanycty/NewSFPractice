from django.contrib import admin
from .models import MachineModel, EngineModel, TransmissionModel, DriveAxleModel, SteeringAxleModel, MaintenanceType, \
    BreakdownType, RecoveryMethod, Machine, Maintenance, Reclamation

# Register your models here.
admin.site.register(MachineModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(DriveAxleModel)
admin.site.register(SteeringAxleModel)
admin.site.register(MaintenanceType)
admin.site.register(BreakdownType)
admin.site.register(RecoveryMethod)
admin.site.register(Machine)
admin.site.register(Maintenance)
admin.site.register(Reclamation)
