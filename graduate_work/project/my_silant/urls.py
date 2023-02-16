from django.urls import path
from .views import MachinesList, MachineDetail, MachineModelDetail, EngineModelDetail, TransmissionModelDetail, \
    DriveAxleModelDetail, SteeringAxleModelDetail, MaintenanceTypeDetail, BreakdownTypeDetail, RecoveryMethodDetail, \
    MaintenanceCreate, MaintenanceDetail, ReclamationDetail, MachineCreate, MachineUpdate, ReclamationCreate, \
    MachineModelCreate, EngineModelCreate, TransmissionModelCreate, DriveAxleModelCreate, SteeringAxleModelCreate, \
    MaintenanceTypeCreate, BreakdownTypeCreate, RecoveryMethodCreate, MaintenanceUpdate, ReclamationUpdate

urlpatterns = [
    path('', MachinesList.as_view(), name='machines_list'),
    path('maintenance/<int:pk>/', MaintenanceDetail.as_view(), name='maintenance_detail'),
    path('reclamation/<int:pk>/', ReclamationDetail.as_view(), name='reclamation_detail'),
    path('machine_model/add', MachineModelCreate.as_view(), name='machine_model_create'),
    path('engine_model/add', EngineModelCreate.as_view(), name='engine_model_create'),
    path('transmission_model/add', TransmissionModelCreate.as_view(), name='transmission_model_create'),
    path('drive_axle_model/add', DriveAxleModelCreate.as_view(), name='drive_axle_model_create'),
    path('steering_axle_model/add', SteeringAxleModelCreate.as_view(), name='steering_axle_model_create'),
    path('maintenance_type/add', MaintenanceTypeCreate.as_view(), name='maintenance_type_create'),
    path('breakdown_type/add', BreakdownTypeCreate.as_view(), name='breakdown_type_create'),
    path('recovery_method/add', RecoveryMethodCreate.as_view(), name='recovery_method_create'),
    path('machine/add', MachineCreate.as_view(), name='machine_create'),
    path('reclamation/add', ReclamationCreate.as_view(), name='reclamation_create'),
    path('reclamation/<int:pk>/edit/', ReclamationUpdate.as_view(), name='reclamation_update'),
    path('machine/<int:pk>/edit/', MachineUpdate.as_view(), name='machine_update'),
    path('maintenance/add', MaintenanceCreate.as_view(), name='maintenance_create'),
    path('maintenance/<int:pk>/edit/', MaintenanceUpdate.as_view(), name='maintenance_update'),
    path('machine/<int:pk>/', MachineDetail.as_view(), name='machine_detail'),
    path('machine_model/<int:pk>/', MachineModelDetail.as_view(), name='machine_model'),
    path('engine_model/<int:pk>/', EngineModelDetail.as_view(), name='engine_model'),
    path('transmission_model/<int:pk>/', TransmissionModelDetail.as_view(), name='transmission_model'),
    path('drive_axle_model/<int:pk>/', DriveAxleModelDetail.as_view(), name='drive_axle_model'),
    path('steering_axle_model/<int:pk>/', SteeringAxleModelDetail.as_view(), name='steering_axle_model'),
    path('maintenance_type/<int:pk>/', MaintenanceTypeDetail.as_view(), name='maintenance_type'),
    path('breakdown_type/<int:pk>/', BreakdownTypeDetail.as_view(), name='breakdown_type'),
    path('recovery_method/<int:pk>/', RecoveryMethodDetail.as_view(), name='recovery_method'),
]
