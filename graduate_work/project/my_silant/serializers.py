from rest_framework import serializers
from .models import Machine, Maintenance, Reclamation


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id', 'machine_model', 'machine_factory_number', 'engine_model', 'engine_factory_number',
                  'transmission_model', 'transmission_factory_number', 'drive_axle_model', 'drive_axle_factory_number',
                  'steering_axle_model', 'steering_axle_factory_number', 'supply_contract', 'shipping_date',
                  'end_user', 'delivery_address', 'complete_set', 'client', 'service_company']


class MachineSerializerGuest(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id', 'machine_model', 'machine_factory_number', 'engine_model', 'engine_factory_number',
                  'transmission_model', 'transmission_factory_number', 'drive_axle_model', 'drive_axle_factory_number',
                  'steering_axle_model', 'steering_axle_factory_number', ]


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ['id', 'maintenance_type', 'maintenance_date', 'running_time', 'work_order_number',
                  'work_order_date', 'maintenance_service_company', 'maintenance_machine', ]


class ReclamationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamation
        fields = ['id', 'breakdown_date', 'running_time', 'broken_node', 'breakdown_description',
                  'recovery_method', 'spare_parts_used', 'recovery_date', 'downtime',
                  'reclamation_machine', 'reclamation_service_company', ]


class BlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = []
