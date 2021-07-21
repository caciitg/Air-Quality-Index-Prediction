from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    # def ready(self):
    #     print("Scheduler from app starting")
    #     from .apscheduler import data_update_autojob
    #     data_update_autojob.start()