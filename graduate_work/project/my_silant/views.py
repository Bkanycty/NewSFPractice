from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics

from .models import Machine, Maintenance, Reclamation, MaintenanceType, MachineModel, EngineModel, TransmissionModel, \
    DriveAxleModel, SteeringAxleModel, BreakdownType, RecoveryMethod
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .filters import MachineFilter
from .forms import MaintenanceForm, MachineForm, ReclamationForm, MachineModelForm, EngineModelForm, \
    TransmissionModelForm, DriveAxleModelForm, SteeringAxleModelForm, MaintenanceTypeForm, BreakdownTypeForm, \
    RecoveryMethodForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect


class ManagerTools(TemplateView):
    template_name = 'group_templates/manager_tools.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['machines'] = Machine.objects.order_by('shipping_date')
        context['maintenances'] = Maintenance.objects.order_by('maintenance_date')
        context['reclamations'] = Reclamation.objects.order_by('breakdown_date')

        context['clients'] = User.objects.filter(groups=1)
        context['service_companies'] = User.objects.filter(groups=2)

        context['machine_models'] = MachineModel.objects.all()
        context['engine_models'] = EngineModel.objects.all()
        context['transmission_models'] = TransmissionModel.objects.all()
        context['drive_axle_models'] = DriveAxleModel.objects.all()
        context['steering_axle_models'] = SteeringAxleModel.objects.all()
        context['maintenance_types'] = MaintenanceType.objects.all()
        context['broken_nodes'] = BreakdownType.objects.all()
        context['recovery_methods'] = RecoveryMethod.objects.all()

        return context


class MachinesList(ListView):
    model = Machine
    template_name = 'Main.html'
    context_object_name = 'machines'
    queryset = Machine.objects.order_by('-shipping_date')

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            machine_factory_number = self.request.GET.get('machine_factory_number')
            object_list = Machine.objects.filter(machine_factory_number__exact=machine_factory_number)
            return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Для определения принадлежности к группе
        context['is_admin'] = self.request.user.is_superuser
        context['is_not_authenticated'] = not self.request.user.is_authenticated
        context['is_manager'] = self.request.user.groups.filter(name='managers').exists()
        context['is_client'] = self.request.user.groups.filter(name='clients').exists()
        context['is_service'] = self.request.user.groups.filter(name='service_companies').exists()

        # Для менеджеров
        context['machines'] = Machine.objects.order_by('shipping_date')
        context['maintenances'] = Maintenance.objects.order_by('maintenance_date')
        context['reclamations'] = Reclamation.objects.order_by('breakdown_date')

        context['clients'] = User.objects.filter(groups=1)
        context['service_companies'] = User.objects.filter(groups=2)

        context['machine_models'] = MachineModel.objects.all()
        context['engine_models'] = EngineModel.objects.all()
        context['transmission_models'] = TransmissionModel.objects.all()
        context['drive_axle_models'] = DriveAxleModel.objects.all()
        context['steering_axle_models'] = SteeringAxleModel.objects.all()
        context['maintenance_types'] = MaintenanceType.objects.all()
        context['broken_nodes'] = BreakdownType.objects.all()
        context['recovery_methods'] = RecoveryMethod.objects.all()

        # Для клиентов:
        context['client_machines'] = Machine.objects.filter(client__username=self.request.user.username).order_by(
            'shipping_date')
        # Для опций в форме фильтрации на странице клиента:
        # Вкладка "Общая инфо"
        context['client_machine_model_set'] = set(
            machine.machine_model for machine in Machine.objects.filter(client=self.request.user.id))
        context['client_engine_model_set'] = set(
            machine.engine_model for machine in Machine.objects.filter(client=self.request.user.id))
        context['client_transmission_model_set'] = set(
            machine.transmission_model for machine in Machine.objects.filter(client=self.request.user.id))
        context['client_drive_axle_model_set'] = set(
            machine.drive_axle_model for machine in Machine.objects.filter(client=self.request.user.id))
        context['client_steering_axle_model_set'] = set(
            machine.steering_axle_model for machine in Machine.objects.filter(client=self.request.user.id))
        # Вкладка ТО
        context['client_maintenance_type_set'] = set(
            maintenance.maintenance_type for maintenance in
            Maintenance.objects.filter(maintenance_machine__client=self.request.user.id))
        context['client_service_company_set'] = set(
            maintenance.maintenance_service_company for maintenance in
            Maintenance.objects.filter(maintenance_machine__client=self.request.user.id))
        # Вкладка Рекламации
        context['client_broken_node_set'] = set(reclamation.broken_node for reclamation in Reclamation.objects.filter(
            reclamation_machine__client=self.request.user.id))
        context['client_recovery_method_set'] = set(
            reclamation.recovery_method for reclamation in Reclamation.objects.filter(
                reclamation_machine__client=self.request.user.id))
        context['client_reclamation_service_company_set'] = set(
            reclamation.reclamation_machine.service_company for reclamation in Reclamation.objects.filter(
                reclamation_machine__client=self.request.user.id))

        # Для сервисных компаний
        # Для опций в форме фильтрации на странице клиента:
        # Вкладка "Общая инфо"
        context['service_machine_model_set'] = set(
            machine.machine_model for machine in Machine.objects.filter(service_company=self.request.user.id))
        context['service_engine_model_set'] = set(
            machine.engine_model for machine in Machine.objects.filter(service_company=self.request.user.id))
        context['service_transmission_model_set'] = set(
            machine.transmission_model for machine in Machine.objects.filter(service_company=self.request.user.id))
        context['service_drive_axle_model_set'] = set(
            machine.drive_axle_model for machine in Machine.objects.filter(service_company=self.request.user.id))
        context['service_steering_axle_model_set'] = set(
            machine.steering_axle_model for machine in Machine.objects.filter(service_company=self.request.user.id))
        # Вкладка ТО
        context['service_maintenance_type_set'] = set(
            maintenance.maintenance_type for maintenance in
            Maintenance.objects.filter(maintenance_machine__service_company=self.request.user.id))
        context['service_service_company_set'] = set(
            maintenance.maintenance_service_company for maintenance in
            Maintenance.objects.filter(maintenance_service_company=self.request.user.id))
        # Вкладка Рекламации
        context['service_broken_node_set'] = set(reclamation.broken_node for reclamation in Reclamation.objects.filter(
            reclamation_machine__service_company=self.request.user.id))
        context['service_recovery_method_set'] = set(
            reclamation.recovery_method for reclamation in Reclamation.objects.filter(
                reclamation_machine__service_company=self.request.user.id))
        context['service_reclamation_service_company_set'] = set(
            reclamation.reclamation_machine.service_company for reclamation in Reclamation.objects.filter(
                reclamation_machine__service_company=self.request.user.id))

        # Для фильтрации
        context['machines_filter'] = MachineFilter(self.request.GET,
                                                   queryset=self.get_queryset())

        return context


class MachineDetail(DetailView):
    model = Machine
    template_name = 'detail_templates/machine_detail.html'
    context_object_name = 'machine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authenticated'] = not self.request.user.is_authenticated
        context['is_client'] = self.request.user.groups.filter(name='clients').exists()
        context['is_service'] = self.request.user.groups.filter(name='service_companies').exists()
        context['is_manager'] = self.request.user.groups.filter(name='managers').exists()

        return context


class MachineCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = MachineForm
    model = Machine
    template_name = 'create_templates/machine_create.html'
    permission_required = ('my_silant.add_machine',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = User.objects.filter(groups=1)
        context['service_companies'] = User.objects.filter(groups=2)

        return context

    def post(self, request, *args, **kwargs):
        machine_model = request.POST['machine_model']
        machine_factory_number = request.POST['machine_factory_number']
        engine_model = request.POST['engine_model']
        engine_factory_number = request.POST['engine_factory_number']
        transmission_model = request.POST['transmission_model']
        transmission_factory_number = request.POST['transmission_factory_number']
        drive_axle_model = request.POST['drive_axle_model']
        drive_axle_factory_number = request.POST['drive_axle_factory_number']
        steering_axle_model = request.POST['steering_axle_model']
        steering_axle_factory_number = request.POST['steering_axle_factory_number']
        supply_contract = request.POST['supply_contract']
        shipping_date = request.POST['shipping_date']
        end_user = request.POST['end_user']
        delivery_address = request.POST['delivery_address']
        complete_set = request.POST['complete_set']
        client = request.POST['client']
        service_company = request.POST['service_company']
        new_machine = Machine.objects.create(machine_model=MachineModel.objects.get(id=machine_model),
                                             machine_factory_number=machine_factory_number,
                                             engine_model=EngineModel.objects.get(id=engine_model),
                                             engine_factory_number=engine_factory_number,
                                             transmission_model=TransmissionModel.objects.get(id=transmission_model),
                                             transmission_factory_number=transmission_factory_number,
                                             drive_axle_model=DriveAxleModel.objects.get(id=drive_axle_model),
                                             drive_axle_factory_number=drive_axle_factory_number,
                                             steering_axle_model=SteeringAxleModel.objects.get(id=steering_axle_model),
                                             steering_axle_factory_number=steering_axle_factory_number,
                                             supply_contract=supply_contract, shipping_date=shipping_date,
                                             end_user=end_user, delivery_address=delivery_address,
                                             complete_set=complete_set, client=User.objects.get(id=client),
                                             service_company=User.objects.get(id=service_company)
                                             )

        new_machine.save()

        return redirect('machines_list')


class MachineUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Machine
    template_name = 'create_templates/machine_create.html'
    form_class = MachineForm
    permission_required = ('my_silant.change_machine',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = User.objects.filter(groups=1)
        context['service_companies'] = User.objects.filter(groups=2)

        return context

    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return Machine.objects.get(pk=_id)


class MachineDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Machine
    template_name = 'delete_templates/machine_delete.html'
    success_url = "/"
    permission_required = ('my_silant.delete_machine',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('pk')
        context['elem_to_delete'] = Machine.objects.get(id=_id)

        return context


class MaintenanceDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Maintenance
    template_name = 'detail_templates/maintenance_detail.html'
    context_object_name = 'maintenance'
    permission_required = ('my_silant.view_maintenance',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authenticated'] = not self.request.user.is_authenticated
        context['is_client'] = self.request.user.groups.filter(name='clients').exists()
        context['is_service'] = self.request.user.groups.filter(name='service_companies').exists()
        context['is_manager'] = self.request.user.groups.filter(name='managers').exists()

        return context


class MaintenanceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = MaintenanceForm
    model = Maintenance
    template_name = 'create_templates/maintenance_create.html'
    permission_required = ('my_silant.add_maintenance',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_machines'] = Machine.objects.filter(client__username=self.request.user.username).order_by(
            'shipping_date')
        context['all_machines'] = Machine.objects.all()
        context['service_machines'] = Machine.objects.filter(
            service_company__username=self.request.user.username).order_by(
            'shipping_date')
        context['is_client'] = self.request.user.groups.filter(name='clients').exists()
        context['is_service'] = self.request.user.groups.filter(name='service_companies').exists()
        context['is_manager'] = self.request.user.groups.filter(name='managers').exists()
        context['is_admin'] = self.request.user.is_superuser
        context['service_companies'] = User.objects.filter(groups=2)

        return context

    def post(self, request, *args, **kwargs):
        maintenance_type = request.POST['maintenance_type']
        maintenance_date = request.POST['maintenance_date']
        running_time = request.POST['running_time']
        work_order_number = request.POST['work_order_number']
        work_order_date = request.POST['work_order_date']
        maintenance_service_company = request.POST['maintenance_service_company']
        maintenance_machine = request.POST['maintenance_machine']
        new_maintenance = Maintenance.objects.create(maintenance_type=MaintenanceType.objects.get(id=maintenance_type),
                                                     maintenance_date=maintenance_date, running_time=running_time,
                                                     work_order_number=work_order_number,
                                                     work_order_date=work_order_date,
                                                     maintenance_service_company=User.objects.get(
                                                         id=maintenance_service_company),
                                                     maintenance_machine=Machine.objects.get(id=maintenance_machine)
                                                     )

        new_maintenance.save()

        return redirect('machines_list')


class MaintenanceUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'create_templates/maintenance_create.html'
    form_class = MaintenanceForm
    permission_required = ('my_silant.change_maintenance',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_machines'] = Machine.objects.filter(client__username=self.request.user.username).order_by(
            'shipping_date')
        context['all_machines'] = Machine.objects.all()
        context['service_machines'] = Machine.objects.filter(
            service_company__username=self.request.user.username).order_by(
            'shipping_date')
        context['is_client'] = self.request.user.groups.filter(name='clients').exists()
        context['is_service'] = self.request.user.groups.filter(name='service_companies').exists()
        context['is_manager'] = self.request.user.groups.filter(name='managers').exists()
        context['is_admin'] = self.request.user.is_superuser
        context['service_companies'] = User.objects.filter(groups=2)

        return context

    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return Maintenance.objects.get(pk=_id)


class MaintenanceDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Maintenance
    template_name = 'delete_templates/maintenance_delete.html'
    success_url = "/"
    permission_required = ('my_silant.delete_maintenance',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('pk')
        context['elem_to_delete'] = Maintenance.objects.get(id=_id)

        return context


class ReclamationDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Reclamation
    template_name = 'detail_templates/reclamation_detail.html'
    context_object_name = 'reclamation'
    permission_required = ('my_silant.view_reclamations',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authenticated'] = not self.request.user.is_authenticated
        context['is_client'] = self.request.user.groups.filter(name='clients').exists()
        context['is_service'] = self.request.user.groups.filter(name='service_companies').exists()
        context['is_manager'] = self.request.user.groups.filter(name='managers').exists()

        return context


class ReclamationCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ReclamationForm
    model = Reclamation
    template_name = 'create_templates/reclamation_create.html'
    permission_required = ('my_silant.add_reclamations',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_machines'] = Machine.objects.all()
        context['service_machines'] = Machine.objects.filter(
            service_company__username=self.request.user.username).order_by(
            'shipping_date')
        context['is_service'] = self.request.user.groups.filter(name='service_companies').exists()
        context['is_manager'] = self.request.user.groups.filter(name='managers').exists()
        context['service_companies'] = User.objects.filter(groups=2)

        return context

    def post(self, request, *args, **kwargs):
        breakdown_date = request.POST['breakdown_date']
        running_time = request.POST['running_time']
        broken_node = request.POST['broken_node']
        breakdown_description = request.POST['breakdown_description']
        recovery_method = request.POST['recovery_method']
        spare_parts_used = request.POST['spare_parts_used']
        recovery_date = request.POST['recovery_date'] if request.POST['recovery_date'] != '' else None
        reclamation_machine = request.POST['reclamation_machine']
        reclamation_service_company = request.POST['reclamation_service_company']

        if self.request.user.groups.filter(name='service_companies').exists():
            new_reclamation = Reclamation.objects.create(breakdown_date=breakdown_date,
                                                         running_time=running_time,
                                                         broken_node=BreakdownType.objects.get(id=broken_node),
                                                         breakdown_description=breakdown_description,
                                                         recovery_method=RecoveryMethod.objects.get(id=recovery_method),
                                                         spare_parts_used=spare_parts_used,
                                                         recovery_date=recovery_date,
                                                         reclamation_machine=Machine.objects.get(
                                                             id=reclamation_machine),
                                                         reclamation_service_company=User.objects.get(
                                                             id=self.request.user.id)
                                                         )
        elif self.request.user.groups.filter(name='managers').exists():
            new_reclamation = Reclamation.objects.create(breakdown_date=breakdown_date,
                                                         running_time=running_time,
                                                         broken_node=BreakdownType.objects.get(id=broken_node),
                                                         breakdown_description=breakdown_description,
                                                         recovery_method=RecoveryMethod.objects.get(id=recovery_method),
                                                         spare_parts_used=spare_parts_used,
                                                         recovery_date=recovery_date,
                                                         reclamation_machine=Machine.objects.get(
                                                             id=reclamation_machine),
                                                         reclamation_service_company=User.objects.get(
                                                             id=reclamation_service_company)
                                                         )
        new_reclamation.save()

        return redirect('machines_list')


class ReclamationUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'create_templates/reclamation_create.html'
    form_class = ReclamationForm
    permission_required = ('my_silant.change_reclamation',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_machines'] = Machine.objects.all()
        context['service_machines'] = Machine.objects.filter(
            service_company__username=self.request.user.username).order_by(
            'shipping_date')
        context['is_service'] = self.request.user.groups.filter(name='service_companies').exists()
        context['is_manager'] = self.request.user.groups.filter(name='managers').exists()
        context['service_companies'] = User.objects.filter(groups=2)

        return context

    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return Reclamation.objects.get(pk=_id)


class ReclamationDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Reclamation
    template_name = 'delete_templates/maintenance_delete.html'
    success_url = "/"
    permission_required = ('my_silant.delete_reclamations',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('pk')
        context['elem_to_delete'] = Reclamation.objects.get(id=_id)

        return context


class MachineModelDetail(DetailView):
    model = MachineModel
    template_name = 'detail_templates/machine_model_detail.html'
    context_object_name = 'machine_model'


class MachineModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = MachineModelForm
    model = MachineModel
    template_name = 'create_templates/node_create.html'
    permission_required = ('my_silant.add_machinemodel',)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        description = request.POST['description']
        new_node = MachineModel.objects.create(name=name, description=description)
        new_node.save()

        return redirect('manager_tools')


class MachineModelUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = MachineModel
    template_name = 'create_templates/node_create.html'
    form_class = MachineModelForm
    permission_required = ('my_silant.change_machinemodel',)

    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return MachineModel.objects.get(pk=_id)


class MachineModelDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = MachineModel
    template_name = 'delete_templates/delete.html'
    success_url = "/"
    permission_required = ('my_silant.delete_machinemodel',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('pk')
        context['elem_to_delete'] = MachineModel.objects.get(id=_id)

        return context


class EngineModelDetail(DetailView):
    model = EngineModel
    template_name = 'detail_templates/engine_model_detail.html'
    context_object_name = 'engine_model'


class EngineModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = EngineModelForm
    model = EngineModel
    template_name = 'create_templates/node_create.html'
    permission_required = ('my_silant.add_enginemodel',)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        description = request.POST['description']
        new_node = EngineModel.objects.create(name=name, description=description)
        new_node.save()

        return redirect('manager_tools')


class EngineModelUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = EngineModel
    template_name = 'create_templates/node_create.html'
    form_class = EngineModelForm
    permission_required = ('my_silant.change_enginemodel',)

    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return EngineModel.objects.get(pk=_id)


class EngineModelDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = EngineModel
    template_name = 'delete_templates/delete.html'
    success_url = "/"
    permission_required = ('my_silant.delete_enginemodel',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('pk')
        context['elem_to_delete'] = EngineModel.objects.get(id=_id)

        return context


class TransmissionModelDetail(DetailView):
    model = TransmissionModel
    template_name = 'detail_templates/transmission_model_detail.html'
    context_object_name = 'transmission_model'


class TransmissionModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = TransmissionModelForm
    model = TransmissionModel
    template_name = 'create_templates/node_create.html'
    permission_required = ('my_silant.add_transmissionmodel',)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        description = request.POST['description']
        new_node = TransmissionModel.objects.create(name=name, description=description)
        new_node.save()

        return redirect('manager_tools')


class TransmissionModelUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TransmissionModel
    template_name = 'create_templates/node_create.html'
    form_class = TransmissionModelForm
    permission_required = ('my_silant.change_transmissionmodel',)

    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return TransmissionModel.objects.get(pk=_id)


class TransmissionModelDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = TransmissionModel
    template_name = 'delete_templates/delete.html'
    success_url = "/"
    permission_required = ('my_silant.delete_transmissionmodel',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('pk')
        context['elem_to_delete'] = TransmissionModel.objects.get(id=_id)

        return context


class DriveAxleModelDetail(DetailView):
    model = DriveAxleModel
    template_name = 'detail_templates/drive_axle_model_detail.html'
    context_object_name = 'drive_axle_model'


class DriveAxleModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = DriveAxleModelForm
    model = DriveAxleModel
    template_name = 'create_templates/node_create.html'
    permission_required = ('my_silant.add_driveaxlemodel',)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        description = request.POST['description']
        new_node = DriveAxleModel.objects.create(name=name, description=description)
        new_node.save()

        return redirect('manager_tools')


class DriveAxleModelUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = DriveAxleModel
    template_name = 'create_templates/node_create.html'
    form_class = DriveAxleModelForm
    permission_required = ('my_silant.change_driveaxlemodel',)

    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return DriveAxleModel.objects.get(pk=_id)


class DriveAxleModelDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = DriveAxleModel
    template_name = 'delete_templates/delete.html'
    success_url = "/"
    permission_required = ('my_silant.delete_driveaxlemodel',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('pk')
        context['elem_to_delete'] = DriveAxleModel.objects.get(id=_id)

        return context


class SteeringAxleModelDetail(DetailView):
    model = SteeringAxleModel
    template_name = 'detail_templates/steering_axle_model_detail.html'
    context_object_name = 'steering_axle_model'


class SteeringAxleModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SteeringAxleModelForm
    model = SteeringAxleModel
    template_name = 'create_templates/node_create.html'
    permission_required = ('my_silant.add_steeringaxlemodel',)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        description = request.POST['description']
        new_node = SteeringAxleModel.objects.create(name=name, description=description)
        new_node.save()

        return redirect('manager_tools')


class SteeringAxleModelUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = SteeringAxleModel
    template_name = 'create_templates/node_create.html'
    form_class = SteeringAxleModelForm
    permission_required = ('my_silant.change_steeringaxlemodel',)

    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return SteeringAxleModel.objects.get(pk=_id)


class SteeringAxleModelDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = SteeringAxleModel
    template_name = 'delete_templates/delete.html'
    success_url = "/"
    permission_required = ('my_silant.delete_steeringaxlemodel',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('pk')
        context['elem_to_delete'] = SteeringAxleModel.objects.get(id=_id)

        return context


class MaintenanceTypeDetail(DetailView):
    model = MaintenanceType
    template_name = 'detail_templates/maintenance_type_detail.html'
    context_object_name = 'maintenance_type'


class MaintenanceTypeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = MaintenanceTypeForm
    model = MaintenanceType
    template_name = 'create_templates/node_create.html'
    permission_required = ('my_silant.add_maintenancetype',)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        description = request.POST['description']
        new_node = MaintenanceType.objects.create(name=name, description=description)
        new_node.save()

        return redirect('manager_tools')


class MaintenanceTypeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = MaintenanceType
    template_name = 'create_templates/node_create.html'
    form_class = MaintenanceTypeForm
    permission_required = ('my_silant.change_maintenancetype',)

    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return MaintenanceType.objects.get(pk=_id)


class MaintenanceTypeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = MaintenanceType
    template_name = 'delete_templates/delete.html'
    success_url = "/"
    permission_required = ('my_silant.delete_maintenancetype',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('pk')
        context['elem_to_delete'] = MaintenanceType.objects.get(id=_id)

        return context


class BreakdownTypeDetail(DetailView):
    model = BreakdownType
    template_name = 'detail_templates/breakdown_type_detail.html'
    context_object_name = 'breakdown_type'


class BreakdownTypeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = BreakdownTypeForm
    model = BreakdownType
    template_name = 'create_templates/node_create.html'
    permission_required = ('my_silant.add_breakdowntype',)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        description = request.POST['description']
        new_node = BreakdownType.objects.create(name=name, description=description)
        new_node.save()

        return redirect('manager_tools')


class BreakdownTypeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = BreakdownType
    template_name = 'create_templates/node_create.html'
    form_class = BreakdownTypeForm
    permission_required = ('my_silant.change_breakdowntype',)

    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return BreakdownType.objects.get(pk=_id)


class BreakdownTypeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = BreakdownType
    template_name = 'delete_templates/delete.html'
    success_url = "/"
    permission_required = ('my_silant.delete_breakdowntype',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('pk')
        context['elem_to_delete'] = BreakdownType.objects.get(id=_id)

        return context


class RecoveryMethodDetail(DetailView):
    model = RecoveryMethod
    template_name = 'detail_templates/recovery_method_detail.html'
    context_object_name = 'recovery_method'


class RecoveryMethodCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RecoveryMethodForm
    model = RecoveryMethod
    template_name = 'create_templates/node_create.html'
    permission_required = ('my_silant.add_recoverymethod',)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        description = request.POST['description']
        new_node = RecoveryMethod.objects.create(name=name, description=description)
        new_node.save()

        return redirect('manager_tools')


class RecoveryMethodUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = RecoveryMethod
    template_name = 'create_templates/node_create.html'
    form_class = RecoveryMethodForm
    permission_required = ('my_silant.change_recoverymethod',)

    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return RecoveryMethod.objects.get(pk=_id)


class RecoveryMethodDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = RecoveryMethod
    template_name = 'delete_templates/delete.html'
    success_url = "/"
    permission_required = ('my_silant.delete_recoverymethod',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('pk')
        context['elem_to_delete'] = RecoveryMethod.objects.get(id=_id)

        return context


class MachineListApiView(generics.ListAPIView):
    queryset = Machine.objects.order_by('-shipping_date')

    def get_serializer_class(self):
        if not self.request.user.is_authenticated:
            serializer_class = MachineSerializerGuest
            return serializer_class
        else:
            serializer_class = MachineSerializer
            return serializer_class

    def get_queryset(self):

        if not self.request.user.is_authenticated:
            machine_factory_number = self.request.GET.get('machine_factory_number')
            queryset = Machine.objects.filter(machine_factory_number__exact=machine_factory_number)
            return queryset

        elif self.request.user.is_superuser or self.request.user.groups.filter(name='managers').exists():
            queryset = Machine.objects.order_by('-shipping_date')
            return queryset

        elif self.request.user.groups.filter(name='clients').exists():
            queryset = Machine.objects.filter(client=self.request.user.id).order_by(
                'shipping_date')
            return queryset

        elif self.request.user.groups.filter(name='service_companies').exists():
            queryset = Machine.objects.filter(service_company=self.request.user.id).order_by(
                'shipping_date')
            return queryset


class MaintenanceListApiView(generics.ListAPIView):
    queryset = Maintenance.objects.order_by('maintenance_date')

    def get_serializer_class(self):
        if not self.request.user.is_authenticated:
            serializer_class = BlankSerializer
            return serializer_class
        else:
            serializer_class = MaintenanceSerializer
            return serializer_class

    def get_queryset(self):

        if not self.request.user.is_authenticated:
            queryset = []
            return queryset

        elif self.request.user.is_superuser or self.request.user.groups.filter(name='managers').exists():
            queryset = Maintenance.objects.order_by('maintenance_date')
            return queryset

        elif self.request.user.groups.filter(name='clients').exists():
            queryset = Maintenance.objects.filter(maintenance_machine__client=self.request.user.id).order_by(
                'maintenance_date')
            return queryset

        elif self.request.user.groups.filter(name='service_companies').exists():
            queryset = Maintenance.objects.filter(maintenance_service_company=self.request.user.id).order_by(
                'maintenance_date')
            return queryset


class ReclamationListApiView(generics.ListAPIView):
    queryset = Reclamation.objects.order_by('breakdown_date')

    def get_serializer_class(self):
        if not self.request.user.is_authenticated:
            serializer_class = BlankSerializer
            return serializer_class
        else:
            serializer_class = ReclamationSerializer
            return serializer_class

    def get_queryset(self):

        if not self.request.user.is_authenticated:
            queryset = []
            return queryset

        elif self.request.user.is_superuser or self.request.user.groups.filter(name='managers').exists():
            queryset = Reclamation.objects.order_by('breakdown_date')
            return queryset

        elif self.request.user.groups.filter(name='clients').exists():
            queryset = Reclamation.objects.filter(reclamation_machine__client=self.request.user.id).order_by(
                'breakdown_date')
            return queryset

        elif self.request.user.groups.filter(name='service_companies').exists():
            queryset = Reclamation.objects.filter(reclamation_service_company=self.request.user.id).order_by(
                'breakdown_date')
            return queryset
