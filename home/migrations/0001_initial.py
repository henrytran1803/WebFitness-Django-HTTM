# Generated by Django 4.2.5 on 2023-10-18 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150, unique=True)),
                ('first_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150)),
                ('last_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150)),
                ('email', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bodymeasurements',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('measurementdate', models.DateField(blank=True, db_column='MeasurementDate', null=True)),
                ('age', models.IntegerField(blank=True, db_column='Age', null=True)),
                ('weight', models.DecimalField(blank=True, db_column='Weight', decimal_places=2, max_digits=5, null=True)),
                ('height', models.DecimalField(blank=True, db_column='Height', decimal_places=2, max_digits=5, null=True)),
                ('neck', models.DecimalField(blank=True, db_column='Neck', decimal_places=2, max_digits=5, null=True)),
                ('chest', models.DecimalField(blank=True, db_column='Chest', decimal_places=2, max_digits=5, null=True)),
                ('abdomen', models.DecimalField(blank=True, db_column='Abdomen', decimal_places=2, max_digits=5, null=True)),
                ('hip', models.DecimalField(blank=True, db_column='Hip', decimal_places=2, max_digits=5, null=True)),
                ('thigh', models.DecimalField(blank=True, db_column='Thigh', decimal_places=2, max_digits=5, null=True)),
                ('knee', models.DecimalField(blank=True, db_column='Knee', decimal_places=2, max_digits=5, null=True)),
                ('ankle', models.DecimalField(blank=True, db_column='Ankle', decimal_places=2, max_digits=5, null=True)),
                ('biceps', models.DecimalField(blank=True, db_column='Biceps', decimal_places=2, max_digits=5, null=True)),
                ('forearm', models.DecimalField(blank=True, db_column='Forearm', decimal_places=2, max_digits=5, null=True)),
                ('wrist', models.DecimalField(blank=True, db_column='Wrist', decimal_places=2, max_digits=5, null=True)),
                ('density', models.DecimalField(blank=True, db_column='Density', decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'db_table': 'BodyMeasurements',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserPred',
            fields=[
                ('body', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='home.bodymeasurements')),
                ('bdf', models.FloatField(blank=True, null=True)),
                ('tdee', models.IntegerField(blank=True, null=True)),
                ('bmi', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_pred',
                'managed': False,
            },
        ),
    ]
