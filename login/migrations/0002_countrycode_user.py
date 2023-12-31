# Generated by Django 4.2.5 on 2023-10-16 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryCode',
            fields=[
                ('country_code', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=7, primary_key=True, serialize=False)),
                ('country_name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=10, null=True)),
            ],
            options={
                'db_table': 'country_code',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='login.account')),
                ('f_name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50, null=True)),
                ('l_name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50, null=True)),
                ('email', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50, null=True)),
                ('phone', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=10, null=True)),
                ('gender', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=1, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
