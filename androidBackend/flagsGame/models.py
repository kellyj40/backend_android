from django.db import models

# Create your models here.



class DublinFlags(models.Model):

    lat = models.FloatField()
    lng = models.FloatField()
    taken = models.BooleanField()
    def __str__(self):
        return str(self.lat) +" " + str(self.lng)


class DublinOnRun(models.Model):
    flag = models.ForeignKey(DublinFlags, on_delete=models.CASCADE)
    lat_user = models.FloatField()
    lng_user = models.FloatField()



