from .Training_Verification import Train_Model
from django.db.models.signals import post_save
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

