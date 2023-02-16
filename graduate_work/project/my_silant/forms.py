from django import forms
from django.forms import ModelForm
from .models import Maintenance, Machine, Reclamation, MachineModel, EngineModel, TransmissionModel, DriveAxleModel, \
    SteeringAxleModel, MaintenanceType, BreakdownType, RecoveryMethod
from django.contrib.auth.models import User


class MachineForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MachineForm, self, ).__init__(*args, **kwargs)
        self.fields['service_company'].queryset = User.objects.filter(groups=2)

    class Meta:
        model = Machine
        fields = '__all__'


class MaintenanceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MaintenanceForm, self, ).__init__(*args, **kwargs)
        self.fields['maintenance_service_company'].queryset = User.objects.filter(groups=2)

    class Meta:
        model = Maintenance
        fields = ['maintenance_type', 'maintenance_date', 'running_time', 'work_order_number', 'work_order_date',
                  'maintenance_service_company', 'maintenance_machine']


class ReclamationForm(ModelForm):
    class Meta:
        model = Reclamation
        fields = '__all__'


class MachineModelForm(ModelForm):
    class Meta:
        model = MachineModel
        fields = '__all__'


class EngineModelForm(ModelForm):
    class Meta:
        model = EngineModel
        fields = '__all__'


class TransmissionModelForm(ModelForm):
    class Meta:
        model = TransmissionModel
        fields = '__all__'


class DriveAxleModelForm(ModelForm):
    class Meta:
        model = DriveAxleModel
        fields = '__all__'


class SteeringAxleModelForm(ModelForm):
    class Meta:
        model = SteeringAxleModel
        fields = '__all__'


class MaintenanceTypeForm(ModelForm):
    class Meta:
        model = MaintenanceType
        fields = '__all__'


class BreakdownTypeForm(ModelForm):
    class Meta:
        model = BreakdownType
        fields = '__all__'


class RecoveryMethodForm(ModelForm):
    class Meta:
        model = RecoveryMethod
        fields = '__all__'
