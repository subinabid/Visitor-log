from django.db import models

class ntpcusers(models.Model):
    empid = models.IntegerField()
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    Remarks = models.CharField(max_length=50)

class ntpcvisitors(models.Model):
    empid = models.ForeignKey(ntpcusers, on_delete= models.SET("DEL"))
    timein = models.DateTimeField()
    timeout = models.DateTimeField()
    subject = models.TextField()
    remarks = models.TextField()
