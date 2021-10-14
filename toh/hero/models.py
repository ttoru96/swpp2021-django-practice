from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=120)
    age =  models.IntegerField(default=0, blank=True, null=True)
    score =  models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name
    def  introduce(self):
        return f'Hello, my name is {self.name} and my score is 100!'

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