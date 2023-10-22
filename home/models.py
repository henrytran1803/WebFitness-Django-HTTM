from django.db import models

# Create your models here.
class Bodymeasurements(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    measurementdate = models.DateField(db_column='MeasurementDate', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    neck = models.DecimalField(db_column='Neck', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    chest = models.DecimalField(db_column='Chest', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    abdomen = models.DecimalField(db_column='Abdomen', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    hip = models.DecimalField(db_column='Hip', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    thigh = models.DecimalField(db_column='Thigh', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    knee = models.DecimalField(db_column='Knee', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ankle = models.DecimalField(db_column='Ankle', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    biceps = models.DecimalField(db_column='Biceps', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    forearm = models.DecimalField(db_column='Forearm', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    wrist = models.DecimalField(db_column='Wrist', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bodyfatencoded = models.IntegerField(db_column='BodyFatEncoded', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BodyMeasurements'


class UserPred(models.Model):
    body = models.OneToOneField(Bodymeasurements, models.DO_NOTHING, primary_key=True)
    bdf = models.FloatField(blank=True, null=True)
    tdee = models.IntegerField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_pred'


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'