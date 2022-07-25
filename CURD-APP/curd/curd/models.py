from django.db import models

class curdst(models.Model):
    stname = models.CharField(max_length = 100)
    stmail = models.CharField(max_length = 100)
    staddress = models.CharField(max_length = 100)
    stmobile = models.IntegerField()
    stgender = models.CharField(max_length = 1)