from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=-1)
    score = models.IntegerField(default=0)

    def introduce(self):
        print('Hello, my name is {} and my score is {}!'.format(
            self.name, self.score))

    def __str__(self):
        return self.name


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
# Create your models here.
