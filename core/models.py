from django.db import models

class ntpcuser(models.Model):
    empid = models.IntegerField()
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50, blank=True)
    lname = models.CharField(max_length=50, blank=True)
    designation = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    remarks = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return str(self.empid)

class externaluser(models.Model):
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50, blank=True)
    lname = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=50, blank=True)
    remarks = models.CharField(max_length=500, blank=True)
    vcard = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return str(self.fname)

class visitor(models.Model):
    source = models.CharField(max_length=100)
    ntpcuser = models.ForeignKey(ntpcuser, on_delete =  models.CASCADE, blank = True, null = True)
    externaluser = models.ForeignKey(externaluser, on_delete= models.CASCADE, blank = True, null = True)

class meeting(models.Model):
    visitor = models.ForeignKey(visitor, on_delete= models.SET("DEL"))
    timein = models.DateTimeField()
    timeout = models.DateTimeField()
    subject = models.CharField(max_length=200, blank=True)
    remarks = models.TextField(blank=True)