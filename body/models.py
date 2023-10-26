# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Equipmentneeded(models.Model):
    equipmentneededid = models.AutoField(db_column='EquipmentNeededID', primary_key=True)  # Field name made lowercase.
    equipmentneededname = models.CharField(db_column='EquipmentNeededName', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipmentNeeded'


class Exercisetype(models.Model):
    exercisetypeid = models.AutoField(db_column='ExerciseTypeID', primary_key=True)  # Field name made lowercase.
    exercisetypename = models.CharField(db_column='ExerciseTypeName', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExerciseType'


class ExerciseSuggestions(models.Model):
    user_pred = models.OneToOneField('UserPred', models.DO_NOTHING, db_column='user_pred', primary_key=True)  # The composite primary key (user_pred, ExerciseId) found, that is not supported. The first column is selected.
    exerciseid = models.ForeignKey('Exercises', models.DO_NOTHING, db_column='ExerciseId')  # Field name made lowercase.
    reps = models.IntegerField(db_column='Reps', blank=True, null=True)  # Field name made lowercase.
    sets = models.IntegerField(db_column='Sets', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exercise_suggestions'
        unique_together = (('user_pred', 'exerciseid'),)


class Exercises(models.Model):
    exerciseid = models.AutoField(db_column='ExerciseID', primary_key=True)  # Field name made lowercase.
    exercisename = models.CharField(db_column='ExerciseName', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    musclegroup = models.ForeignKey('Musclegroup', models.DO_NOTHING, db_column='MuscleGroup', blank=True, null=True)  # Field name made lowercase.
    exercisetype = models.ForeignKey(Exercisetype, models.DO_NOTHING, db_column='ExerciseType', blank=True, null=True)  # Field name made lowercase.
    equipmentneeded = models.ForeignKey(Equipmentneeded, models.DO_NOTHING, db_column='EquipmentNeeded', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    difficultylevel = models.CharField(db_column='DifficultyLevel', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    repetitions = models.IntegerField(db_column='Repetitions', blank=True, null=True)  # Field name made lowercase.
    sets = models.IntegerField(db_column='Sets', blank=True, null=True)  # Field name made lowercase.
    durationinseconds = models.IntegerField(db_column='DurationInSeconds', blank=True, null=True)  # Field name made lowercase.
    caloriesburnedperminute = models.DecimalField(db_column='CaloriesBurnedPerMinute', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    targetedmuscles = models.CharField(db_column='TargetedMuscles', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageURL', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exercises'


class Musclegroup(models.Model):
    musclegroupid = models.AutoField(db_column='MuscleGroupID', primary_key=True)  # Field name made lowercase.
    musclegroupname = models.CharField(db_column='MuscleGroupName', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MuscleGroup'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DetailEatTrack(models.Model):
    id = models.IntegerField(primary_key=True)  # The composite primary key (id, product) found, that is not supported. The first column is selected.
    product = models.ForeignKey('Products', models.DO_NOTHING, db_column='product')
    serving_size = models.FloatField(blank=True, null=True)
    calories = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail_eat_track'
        unique_together = (('id', 'product'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EatTrack(models.Model):
    track_id = models.IntegerField(unique=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, date) found, that is not supported. The first column is selected.
    date = models.DateField()
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eat_track'
        unique_together = (('user', 'date'),)


class Nutritions(models.Model):
    nutrition_id = models.CharField(primary_key=True, max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    carbohydrates_100g = models.FloatField(blank=True, null=True)
    energy_kcal_100g = models.FloatField(db_column='energy-kcal_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    fat_100g = models.FloatField(blank=True, null=True)
    proteins_100g = models.FloatField(blank=True, null=True)
    sugars_100g = models.FloatField(blank=True, null=True)
    sodium_100g = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nutritions'


class Products(models.Model):
    barcode = models.OneToOneField(Nutritions, models.DO_NOTHING, db_column='barcode', primary_key=True)
    brand = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    product_name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    image_url = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class UserPred(models.Model):
    body = models.OneToOneField(Bodymeasurements, models.DO_NOTHING, primary_key=True)
    bdf = models.FloatField(blank=True, null=True)
    tdee = models.IntegerField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_pred'
