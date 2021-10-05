# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Modules(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    usercreator = models.CharField(db_column='userCreator', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modules'


class Models(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    library = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'models'

    def __str__(self):
        return '{} algo {}'.format(self.name, self.library)
