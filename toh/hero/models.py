from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(blank=True, null=True)
    try:
        score = models.IntegerField(blank=True, null=True)
    except:
        score = 0

    def __str__(self):
        return self.name
    def introduce(self):
        if self.score is None:
            self.score = 0
        return "Hello, my name is " + self.name + " and my score is " + str(self.score) + "!"

class Team(models.Model):
    name = models.CharField(max_length=120)
    leader = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE,
        related_name='leader_set',
    )
    members = models.ManyToManyField(
        Hero,
        related_name='teams',
    )

    def __str__(self):
        return self.name