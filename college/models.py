from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)
    def __str__(self):
        return "%s (%s)" % (self.name, self.hod)

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True)   
    def __str__(self):
        return "%s (%s)" % (self.name, self.branch)

# Create your models here.
class Notice(models.Model):
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add = True)
    subject = models.CharField(max_length=100)
    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True, blank=True)
    def __str__(self):
        return self.subject