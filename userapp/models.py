from django.db import models
from django.conf import settings
from django.db.models.fields import related

# Create your models here.
class  Loginuser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='Loginuser_user')
    session_key= models.CharField(max_length=32,blank=True,null=True)

    def __str__(self) :
        return self.user.username
