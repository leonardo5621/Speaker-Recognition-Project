import os
from .Training_Verification import Train_Model
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import AcousticModel

@receiver(post_save, sender=AcousticModel)
def create_model(sender , instance, created, **kwargs):
    if created:
        Train_Dir = 'media/profile_access/{}_train_data/'.format(instance.user)
        s_rate = instance.sampling_rate
        Model_name = instance.model_name
        Audio_format = instance.audio_format
        print('Creating Acoustic Model')
        Train_Model(Train_Dir, Model_name, s_rate, AudioFormat=Audio_format)

@receiver(pre_delete, sender=AcousticModel)
def delete_file(sender , instance, **kwargs):
    if instance.audio_data:
        if os.path.isfile(instance.audio_data.path):
            dir_name = os.path.dirname(instance.audio_data.path)
            os.remove(instance.audio_data.path)

            model_path = '{0}{1}.model'.format(dir_name, instance.user)
            if os.path.isfile(model_path):
                os.remove(model_path)
            
        
