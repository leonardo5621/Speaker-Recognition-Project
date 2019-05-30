import pandas as pd
import numpy as np
import datetime
import os
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    user_dir = 'profile_access'
    name = instance.username
    path_to_file = 'media/{0}/{1}/{1}.csv'.format(user_dir, name)
    instance.profile.save()
    if os.path.isfile(path_to_file):  
        pass
    else:
        x = datetime.datetime.now()
        YY = x.strftime('%Y')
        dd = x.strftime('%d')
        mm = x.strftime('%B')
        Dt = str(dd+'-'+mm+'-'+YY)
        inform = np.array(['Total-Tentativas','Permitidas','Negadas'])
        today = np.array([Dt]*3)
        mlindex = [today,inform]
        cols = ['User']
        access_data = pd.DataFrame(np.zeros((3,1)),index=mlindex, columns=cols)
        try:
            print('Criando DataFrame')
            access_data.to_csv(path_to_file, index_label=['A','B'])
        except FileNotFoundError:
            print(os.getcwd())
            print('Erro')
