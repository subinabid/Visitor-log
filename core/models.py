from django.db import models

class ntpcusers(models.Model):
    empid = models.IntegerField()
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50, blank=True)
    lname = models.CharField(max_length=50, blank=True)
    designation = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    remarks = models.CharField(max_length=50, blank=True)

class ntpcvisitors(models.Model):
    empid = models.ForeignKey(ntpcusers, on_delete= models.SET("DEL"))
    timein = models.DateTimeField()
    timeout = models.DateTimeField()
    subject = models.TextField()
    remarks = models.TextField()
