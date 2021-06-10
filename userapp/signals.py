from django.contrib.auth import user_logged_in,user_logged_out
from django.dispatch import receiver
from userapp.models import Loginuser

@receiver(user_logged_in)
def on_userlogged_in(sender,**kwargs):
    Loginuser.objects.get_or_create(user=kwargs.get('user'))
    print("Request login!")
    # pass

@receiver(user_logged_out)
def on_userlog_out(sender,**kwargs):
    Loginuser.objects.filter(user=kwargs.get('user')).delete()
    print("Request logout!")