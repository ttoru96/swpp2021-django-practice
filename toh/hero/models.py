from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=25)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.name)

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "age": str(self.age)}
    
    def introduce(self) -> str:
        return f"Hello, my name is {self.name} and my score is {self.score}!"


class Team(models.Model):
    name = models.CharField(max_length=120)
    leader = models.ForeignKey(
        Hero, on_delete=models.CASCADE, related_name="leader_set"
    )
    members = models.ManyToManyField(Hero, related_name="teams")

    def __str__(self) -> str:
        return str(self.name)
