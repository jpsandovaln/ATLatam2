#
# @models.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
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
