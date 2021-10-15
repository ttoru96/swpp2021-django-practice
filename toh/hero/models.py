from django.db import models

class Hero(models.Model):
  name = models.CharField(max_length=120)
  age = models.IntegerField(blank=True, null = True)
  score = models.IntegerField(default=0)

  def __str__(self):
    return 'name:{0} age:{1}' .format(self.name, self.age)
  
  def introduce(self):
    return 'Hello, my name is {0} and my score is {1}!' .format(self.name, self.score)
# Create your models here.
