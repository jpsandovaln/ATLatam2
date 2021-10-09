from django.db import models


# Create your models here.
class Assets(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=100)
    checksum = models.CharField(max_length=100)

    class Meta:
        managed = True

    def __str__(self):
        return 'record {} named {} with path {} and MD5 format {}'.format(self.id, self.name, self.path, self.checksum)