from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Redactor(AbstractUser):
    years_of_experience = models.CharField(max_length=255)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("newspaper:redactor-detail", kwargs={"pk": self.pk})



class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default="Default content")
    published_date = models.DateField(auto_now=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")


    class Meta:
        ordering = ["topic__name"]

    def __str__(self):
        return f"{self.title} {self.published_date} {self.topic} {self.publishers}"
