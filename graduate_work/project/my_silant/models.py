from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class MachineModel(models.Model):
    name = models.CharField(verbose_name='Модель машины', max_length=256, unique=True,
                            help_text='Введите название модели машины')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание модели машины')

    def __str__(self):
        return self.name


class EngineModel(models.Model):
    name = models.CharField(verbose_name='Модель двигателя', max_length=256, unique=True,
                            help_text='Введите название модели двигателя')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание модели двигателя')

    def __str__(self):
        return self.name


class TransmissionModel(models.Model):
    name = models.CharField(verbose_name='Модель трансмиссии', max_length=256, unique=True,
                            help_text='Введите название модели трансмиссии')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание модели трансмиссии')

    def __str__(self):
        return self.name


class DriveAxleModel(models.Model):
    name = models.CharField(verbose_name='Модель ведущего моста', max_length=256, unique=True,
                            help_text='Введите название модели ведущего моста')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание модели ведущего моста')

    def __str__(self):
        return self.name


class SteeringAxleModel(models.Model):
    name = models.CharField(verbose_name='Модель управляемого моста', max_length=256, unique=True,
                            help_text='Введите название модели управляемого моста')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание модели управляемого моста')

    def __str__(self):
        return self.name


class MaintenanceType(models.Model):
    name = models.CharField(verbose_name='Вид ТО', max_length=256, unique=True,
                            help_text='Введите название вида ТО')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание вида ТО')

    def __str__(self):
        return self.name


class BreakdownType(models.Model):
    name = models.CharField(verbose_name='Характер отказа', max_length=256, unique=True,
                            help_text='Введите название характера отказа')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание характера отказа')

    def __str__(self):
        return self.name


class RecoveryMethod(models.Model):
    name = models.CharField(verbose_name='Способ восстановления', max_length=256, unique=True,
                            help_text='Введите название способа восстановления')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание способа восстановления')

    def __str__(self):
        return self.name


class Machine(models.Model):
    machine_model = models.ForeignKey(MachineModel, help_text='выберите из списка', verbose_name='Модель машины',
                                      related_name='machine_model',
                                      on_delete=models.CASCADE)
    machine_factory_number = models.CharField(verbose_name='Зав. № машины', help_text='заполните вручную',
                                              max_length=256, unique=True)

    engine_model = models.ForeignKey(EngineModel, help_text='выберите из списка', verbose_name='Модель двигателя',
                                     related_name='engine_model',
                                     on_delete=models.CASCADE)
    engine_factory_number = models.CharField(verbose_name='Зав. № двигателя', help_text='заполните вручную',
                                             max_length=256, unique=True)
    transmission_model = models.ForeignKey(TransmissionModel, help_text='выберите из списка',
                                           verbose_name='Модель трансмиссии', related_name='transmission_model',
                                           on_delete=models.CASCADE)
    transmission_factory_number = models.CharField(verbose_name='Зав. № трансмиссии', max_length=256,
                                                   help_text='заполните вручную', unique=True)
    drive_axle_model = models.ForeignKey(DriveAxleModel, help_text='выберите из списка',
                                         verbose_name='Модель ведущего моста', related_name='drive_axle_model',
                                         on_delete=models.CASCADE)
    drive_axle_factory_number = models.CharField(verbose_name='Зав. № ведущего моста', max_length=256,
                                                 help_text='заполните вручную', unique=True)
    steering_axle_model = models.ForeignKey(SteeringAxleModel, help_text='выберите из списка',
                                            verbose_name='Модель управляемого моста',
                                            related_name='steering_axle_model',
                                            on_delete=models.CASCADE)
    steering_axle_factory_number = models.CharField(verbose_name='Зав. № управляемого моста', max_length=256,
                                                    help_text='заполните вручную', unique=True)
    supply_contract = models.CharField(verbose_name='Договор поставки №, дата', max_length=256,
                                       help_text='заполните вручную')
    shipping_date = models.DateField(verbose_name='Дата отгрузки с завода')
    end_user = models.CharField(verbose_name='Грузополучатель (конечный потребитель)', max_length=256,
                                help_text='заполните вручную')
    delivery_address = models.CharField(verbose_name='Адрес поставки (эксплуатации)', max_length=256,
                                        help_text='заполните вручную')
    complete_set = models.TextField(verbose_name='Комплектация (доп. опции)', help_text='заполните вручную')
    client = models.ForeignKey(User, verbose_name='Клиент', related_name='client', null=True, blank=True,
                               on_delete=models.CASCADE, help_text='выберите из списка', default=1)
    service_company = models.ForeignKey(User, verbose_name='Сервисная компания',
                                        related_name='service_company', null=True, blank=True, on_delete=models.CASCADE,
                                        help_text='выберите из списка', default=1)

    def __str__(self):
        return f'{self.machine_model}: {self.machine_factory_number}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/machine/{self.id}'


class Maintenance(models.Model):
    maintenance_type = models.ForeignKey(MaintenanceType, help_text='Выберите вид ТО', verbose_name='Вид ТО',
                                         related_name='maintenance_type', on_delete=models.CASCADE)
    maintenance_date = models.DateField(verbose_name='Дата проведения ТО')
    running_time = models.SmallIntegerField(verbose_name='Наработка, м/час')
    work_order_number = models.CharField(max_length=256, verbose_name='№ заказ-наряда',
                                         help_text='Введите № заказ-наряда')
    work_order_date = models.DateField(verbose_name='Дата заказ-наряда')
    maintenance_service_company = models.ForeignKey(User, help_text='Организация, проводившая ТО',
                                                    verbose_name='Организация, проводившая ТО',
                                                    related_name='maintenance_service_company',
                                                    on_delete=models.CASCADE)
    maintenance_machine = models.ForeignKey(Machine, help_text='Выберите обслуживаемую машину',
                                            verbose_name='Обслуживаемая машина',
                                            related_name='maintenance_machine', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.maintenance_machine.id}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/maintenance/{self.id}'


class Reclamation(models.Model):
    breakdown_date = models.DateField(verbose_name='Дата отказа')
    running_time = models.SmallIntegerField(verbose_name='Наработка, м/час')
    broken_node = models.ForeignKey(BreakdownType, help_text='Выберите узел отказа',
                                    verbose_name='Узел отказа',
                                    related_name='broken_node', on_delete=models.CASCADE)
    breakdown_description = models.TextField(verbose_name='Описание отказа', help_text='Введите описание отказа')
    recovery_method = models.ForeignKey(RecoveryMethod, help_text='Выберите способ восстановления',
                                        verbose_name='Способ восстановления',
                                        related_name='recovery_method', on_delete=models.CASCADE)
    spare_parts_used = models.TextField(verbose_name='Использованные запасные части',
                                        help_text='Перечислите использованные запасные части')
    recovery_date = models.DateField(verbose_name='Дата восстановления', null=True, blank=True)

    def downtime(self):
        if type(self.recovery_date) == datetime.date and type(self.breakdown_date) == datetime.date:
            return (self.recovery_date - self.breakdown_date).days
        else:
            return "-"

    reclamation_machine = models.ForeignKey(Machine, help_text='Выберите к какой машине относится обращение',
                                            verbose_name='Машина обращения',
                                            related_name='reclamation_machine', on_delete=models.CASCADE)
    reclamation_service_company = models.ForeignKey(User, verbose_name='Сервисная компания',
                                                    related_name='reclamation_service_company', null=True, blank=True,
                                                    on_delete=models.CASCADE,
                                                    help_text='выберите из списка', default=1)

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/reclamation/{self.id}'
