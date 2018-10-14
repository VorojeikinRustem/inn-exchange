from django.db import models

from django.contrib.auth.models import User


class Inn(models.Model):
    inn = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Inn"
        verbose_name_plural = "Inns"

    def __str__(self):
        return "%s" % self.inn


class Profile(models.Model):
    price = models.DecimalField(max_digits=15, decimal_places=2)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inn = models.ForeignKey(Inn, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return "%s" % self.user
