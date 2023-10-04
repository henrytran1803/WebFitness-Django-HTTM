from django.db import models

# Create your models here.
class Account(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    password = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    roles = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'