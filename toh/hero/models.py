from django.db import models

class Hero(models.Model):
  name = models.CharField(max_length=120)
  age = models.IntegerField(default=0)
  score = models.IntegerField(default=0)

  def __str__(self):
    return self.name

  def introduce(self):
    return 'Hello, my name is ' + self.name + ' and my score is ' + self.score + '!'