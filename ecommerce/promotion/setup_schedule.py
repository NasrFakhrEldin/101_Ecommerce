from django_celery_beat.models import CrontabSchedule, PeriodicTask


def setup_schedule():
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute="0",
        hour="1",
    )

    PeriodicTask.objects.create(
        crontab=schedule,
        task="ecommerce.promotion.tasks.promotion_managment_is_active",
    )
