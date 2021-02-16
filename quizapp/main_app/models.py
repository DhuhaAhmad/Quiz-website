from django.db import models

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=150)
    score = models.IntegerField()
    Time = models.IntegerField()
    winStreak = models.IntegerField()


class Questions(models.Model):
    question = models.CharField(max_length=400)
    type = models.CharField(max_length=150)
    correctAnswer = models.CharField(max_length=150)
    Level = models.CharField(max_length=150)
    hint = models.CharField(max_length=150)

class Category(models.Model):
    name = models.CharField(max_length=150)
