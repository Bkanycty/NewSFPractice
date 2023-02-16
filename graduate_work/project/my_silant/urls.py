from django.urls import path
from .views import *

urlpatterns = [
    path('', MachinesList.as_view(), name='machines_list'),
    path('machine/<int:pk>/', MachineDetail.as_view(), name='machine_detail'),
    path('machine/add', MachineCreate.as_view(), name='machine_create'),
    path('machine/<int:pk>/edit/', MachineUpdate.as_view(), name='machine_update'),

    path('maintenance/<int:pk>/', MaintenanceDetail.as_view(), name='maintenance_detail'),
    path('maintenance/add', MaintenanceCreate.as_view(), name='maintenance_create'),
    path('maintenance/<int:pk>/edit/', MaintenanceUpdate.as_view(), name='maintenance_update'),

    path('reclamation/<int:pk>/', ReclamationDetail.as_view(), name='reclamation_detail'),
    path('reclamation/add', ReclamationCreate.as_view(), name='reclamation_create'),
    path('reclamation/<int:pk>/edit/', ReclamationUpdate.as_view(), name='reclamation_update'),

    path('machine_model/<int:pk>/', MachineModelDetail.as_view(), name='machine_model'),
    path('machine_model/add', MachineModelCreate.as_view(), name='machine_model_create'),
    path('machine_model/<int:pk>/edit', MachineModelUpdate.as_view(), name='machine_model_update'),
    path('machine_model/<int:pk>/delete', MachineModelDelete.as_view(), name='machine_model_delete'),

    path('engine_model/<int:pk>/', EngineModelDetail.as_view(), name='engine_model'),
    path('engine_model/add', EngineModelCreate.as_view(), name='engine_model_create'),
    path('engine_model/<int:pk>/edit', EngineModelUpdate.as_view(), name='engine_model_update'),
    path('engine_model/<int:pk>/delete', EngineModelDelete.as_view(), name='engine_model_delete'),

    path('transmission_model/<int:pk>/', TransmissionModelDetail.as_view(), name='transmission_model'),
    path('transmission_model/add', TransmissionModelCreate.as_view(), name='transmission_model_create'),
    path('transmission_model/<int:pk>/edit', TransmissionModelUpdate.as_view(), name='transmission_model_update'),
    path('transmission_model/<int:pk>/delete', TransmissionModelDelete.as_view(), name='transmission_model_delete'),

    path('drive_axle_model/<int:pk>/', DriveAxleModelDetail.as_view(), name='drive_axle_model'),
    path('drive_axle_model/add', DriveAxleModelCreate.as_view(), name='drive_axle_model_create'),
    path('drive_axle_model/<int:pk>/edit', DriveAxleModelUpdate.as_view(), name='drive_axle_model_update'),
    path('drive_axle_model/<int:pk>/delete', DriveAxleModelDelete.as_view(), name='drive_axle_model_delete'),

    path('steering_axle_model/<int:pk>/', SteeringAxleModelDetail.as_view(), name='steering_axle_model'),
    path('steering_axle_model/add', SteeringAxleModelCreate.as_view(), name='steering_axle_model_create'),
    path('steering_axle_model/<int:pk>/edit', SteeringAxleModelUpdate.as_view(), name='steering_axle_model_update'),
    path('steering_axle_model/<int:pk>/delete', SteeringAxleModelDelete.as_view(), name='steering_axle_model_delete'),

    path('maintenance_type/<int:pk>/', MaintenanceTypeDetail.as_view(), name='maintenance_type'),
    path('maintenance_type/add', MaintenanceTypeCreate.as_view(), name='maintenance_type_create'),
    path('maintenance_type/<int:pk>/edit', MaintenanceTypeUpdate.as_view(), name='maintenance_type_update'),
    path('maintenance_type/<int:pk>/delete', MaintenanceTypeDelete.as_view(), name='maintenance_type_delete'),

    path('breakdown_type/<int:pk>/', BreakdownTypeDetail.as_view(), name='breakdown_type'),
    path('breakdown_type/add', BreakdownTypeCreate.as_view(), name='breakdown_type_create'),
    path('breakdown_type/<int:pk>/edit', BreakdownTypeUpdate.as_view(), name='breakdown_type_update'),
    path('breakdown_type/<int:pk>/delete', BreakdownTypeDelete.as_view(), name='breakdown_type_delete'),

    path('recovery_method/<int:pk>/', RecoveryMethodDetail.as_view(), name='recovery_method'),
    path('recovery_method/add', RecoveryMethodCreate.as_view(), name='recovery_method_create'),
    path('recovery_method/<int:pk>/edit', RecoveryMethodUpdate.as_view(), name='recovery_method_update'),
    path('recovery_method/<int:pk>/delete', RecoveryMethodDelete.as_view(), name='recovery_method_delete'),

    path('manager_tools/', ManagerTools.as_view(), name='manager_tools'),
]
