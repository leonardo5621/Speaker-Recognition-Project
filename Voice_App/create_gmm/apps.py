from django.apps import AppConfig


class CreateGmmConfig(AppConfig):
    name = 'create_gmm'

    def ready(self):
        print('heer')
        import create_gmm.signals
