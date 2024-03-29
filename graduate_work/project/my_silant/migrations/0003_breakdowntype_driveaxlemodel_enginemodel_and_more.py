# Generated by Django 4.1.5 on 2023-01-18 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_silant', '0002_alter_machine_complete_set'),
    ]

    operations = [
        migrations.CreateModel(
            name='BreakdownType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название характера отказа', max_length=256, unique=True, verbose_name='Характер отказа')),
                ('description', models.TextField(help_text='Введите описание характера отказа', verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='DriveAxleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название модели ведущего моста', max_length=256, unique=True, verbose_name='Модель ведущего моста')),
                ('description', models.TextField(help_text='Введите описание модели ведущего моста', verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='EngineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название модели двигателя', max_length=256, unique=True, verbose_name='Модель двигателя')),
                ('description', models.TextField(help_text='Введите описание модели двигателя', verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='MachineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название модели машины', max_length=256, unique=True, verbose_name='Модель машины')),
                ('description', models.TextField(help_text='Введите описание модели машины', verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название вида ТО', max_length=256, unique=True, verbose_name='Вид ТО')),
                ('description', models.TextField(help_text='Введите описание вида ТО', verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название способа восстановления', max_length=256, unique=True, verbose_name='Способ восстановления')),
                ('description', models.TextField(help_text='Введите описание способа восстановления', verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='SteeringAxleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название модели управляемого моста', max_length=256, unique=True, verbose_name='Модель управляемого моста')),
                ('description', models.TextField(help_text='Введите описание модели управляемого моста', verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название модели трансмиссии', max_length=256, unique=True, verbose_name='Модель трансмиссии')),
                ('description', models.TextField(help_text='Введите описание модели трансмиссии', verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakdown_date', models.DateField(verbose_name='Дата отказа')),
                ('running_time', models.SmallIntegerField(verbose_name='Наработка, м/час')),
                ('breakdown_description', models.TextField(help_text='Введите описание отказа', verbose_name='Описание отказа')),
                ('spare_parts_used', models.TextField(help_text='Перечислите используемые запасные части', verbose_name='Используемые запасные части')),
                ('recovery_date', models.DateField(verbose_name='Дата восстановления')),
                ('broken_node', models.ForeignKey(help_text='Выберите узел отказа', on_delete=django.db.models.deletion.CASCADE, related_name='broken_node', to='my_silant.breakdowntype', verbose_name='Узел отказа')),
                ('reclamation_machine', models.ForeignKey(help_text='Выберите к какой машине относится обращение', on_delete=django.db.models.deletion.CASCADE, related_name='reclamation_machine', to='my_silant.machine', verbose_name='Машина обращения')),
                ('recovery_method', models.ForeignKey(help_text='Выберите способ восстановления', on_delete=django.db.models.deletion.CASCADE, related_name='recovery_method', to='my_silant.recoverymethod', verbose_name='Способ восстановления')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_date', models.DateField(verbose_name='Дата проведения ТО')),
                ('running_time', models.SmallIntegerField(verbose_name='Наработка, м/час')),
                ('work_order_number', models.CharField(help_text='Введите № заказ-наряда', max_length=256, verbose_name='№ заказ-наряда')),
                ('work_order_date', models.DateField(verbose_name='Дата заказ-наряда')),
                ('maintenance_machine', models.ForeignKey(help_text='Выберите обслуживаемую машину', on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_machine', to='my_silant.machine', verbose_name='Обслуживаемая машина')),
                ('maintenance_service_company', models.ForeignKey(help_text='Организация, проводившая ТО', on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_service_company', to=settings.AUTH_USER_MODEL, verbose_name='Организация, проводившая ТО')),
                ('maintenance_type', models.ForeignKey(help_text='Выберите вид ТО', on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_type', to='my_silant.maintenancetype', verbose_name='Вид ТО')),
            ],
        ),
        migrations.AlterField(
            model_name='machine',
            name='drive_axle_model',
            field=models.ForeignKey(help_text='Модель ведущего моста', on_delete=django.db.models.deletion.CASCADE, related_name='drive_axle_model', to='my_silant.driveaxlemodel', verbose_name='Модель ведущего моста'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='engine_model',
            field=models.ForeignKey(help_text='Модель двигателя', on_delete=django.db.models.deletion.CASCADE, related_name='engine_model', to='my_silant.enginemodel', verbose_name='Модель двигателя'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='machine_model',
            field=models.ForeignKey(help_text='Модель машины', on_delete=django.db.models.deletion.CASCADE, related_name='machine_model', to='my_silant.machinemodel', verbose_name='Модель машины'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='steering_axle_model',
            field=models.ForeignKey(help_text='Модель управляемого моста', on_delete=django.db.models.deletion.CASCADE, related_name='steering_axle_model', to='my_silant.steeringaxlemodel', verbose_name='Модель управляемого моста'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='transmission_model',
            field=models.ForeignKey(help_text='Модель трансмиссии', on_delete=django.db.models.deletion.CASCADE, related_name='transmission_model', to='my_silant.transmissionmodel', verbose_name='Модель трансмиссии'),
        ),
    ]
