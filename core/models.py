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
    def __str__(self):
        return str(self.empid)

class ntpcvisitors(models.Model):
    empid = models.ForeignKey(ntpcusers, on_delete= models.SET("DEL"))
    timein = models.DateTimeField()
    timeout = models.DateTimeField()
    subject = models.CharField(max_length=200, blank=True)
    remarks = models.TextField(blank=True)
    def __str__(self):
        return str(self.empid)
    
