from django.db import models

# Create your models here.


class Application(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    second_name = models.CharField(max_length=20, blank=False, null=False)
    group = models.CharField(max_length=10, blank=False, null=False)
    phone = models.CharField(max_length=13, blank=False, null=False)
    reason = models.TextField(blank=True)
    money = models.IntegerField(blank=False, null=False, default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}: {} {}".format(self.time, self.first_name, self.second_name)
