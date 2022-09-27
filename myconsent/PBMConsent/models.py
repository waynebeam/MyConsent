from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=400)
    question_number = models.IntegerField()

    def __str__(self):
        return str(self.question_number) + ": " + self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=400)
    display_text = models.CharField(max_length=400)
    description_text = models.CharField(max_length=400)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
