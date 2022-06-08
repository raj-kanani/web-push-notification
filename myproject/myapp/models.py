from django.db import models
from twilio.rest import Client
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json


class Student(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    address = models.CharField(max_length=120)

    def save(self, *args, **kwargs):
        account_sid = 'AC291d18cb63a0783d31db55fc77afce04'
        auth_token = '1ba7775685b7ea66c857909cd8fb8c84'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"hello, you are now login with  - {self.name}, your age  is - {self.age} and your address is - {self.address}",
            from_='+17163174923',
            to='+916353468226'
        )

        print(message.sid)
        return super().save(*args, **kwargs)


class BroadcastNotification(models.Model):
    message = models.TextField()
    broadcast_on = models.DateTimeField()
    sent = models.BooleanField(default=False)

    class Meta:
        ordering = ['-broadcast_on']


@receiver(post_save, sender=BroadcastNotification)
def notification_handler(sender, instance, created, **kwargs):
    # call group_send function directly to send notifications or
    # you can create a dynamic task in celery beat
    if created:
        schedule, created = CrontabSchedule.objects.get_or_create \
            (hour=instance.broadcast_on.hour, minute=instance.broadcast_on.minute,
             day_of_month=instance.broadcast_on.day, month_of_year=instance.broadcast_on.month)
        task = PeriodicTask.objects.create \
            (crontab=schedule, name="broadcast-notification-" + str(instance.id),
             task="myapp.tasks.broadcast_notification",
             args=json.dumps((instance.id,)))


from django.db import models


class Child(models.Model):
    name = models.CharField(max_length=100, verbose_name="Child's First Name and Last Name")
    weight = models.DecimalField(max_digits=5,decimal_places=0)

    class Meta:
        db_table = 'new'
        verbose_name = 'boy'
        verbose_name_plural = 'MY CHILD'

    def __str__(self):
        return self.name
