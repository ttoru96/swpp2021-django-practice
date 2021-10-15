from django.db import models

class Hero(models.Model):
  name = models.CharField(max_length=120)
  age = models.IntegerField(blank=True, null = True)

  def __str__(self):
    return 'name:{0} age:{1}' .format(self.name, self.age)
# Create your models here.
