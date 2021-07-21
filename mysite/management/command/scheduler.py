from ../main.models import Data,Test
from ../main.Ml_model import Ml_model as ml

class Command(BaseCommand):
  """
  Management command for APScheduler
  """

  def handle(self, *args, **kwargs):
    sched = Scheduler()

    @sched.cron_schedule('interval',minutes=1)
    def my_scheduled_job():
        print("My job is running")
        # print("My job is running")
        Test.objects.create(name = "test")
        ml.fun(ml.df)

    sched.start()
    print("Scheduler started")

    # while True:
    #   pass