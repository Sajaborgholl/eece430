from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title


class Question(models.Model): #database table represented by a class
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)