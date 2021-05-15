from django.db import models
from accounts.models import CustomUser
from datetime import date, datetime

# Create your models here.



    
class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    num =  models.IntegerField(blank=True,null=True)
    title = models.TextField()
    option_1 = models.CharField(max_length=500)
    option_2 = models.CharField(max_length=500)
    option_3 = models.CharField(max_length=500)
    option_4 = models.CharField(max_length=500)
    answer = models.IntegerField()
    
    def __str__(self):
        return self.title + '  |   ' + str(self.question_id)
    
    
    
class Quiz(models.Model):
    title = models.CharField(max_length=255,unique=True,db_index=True)
    number_of_questions = models.IntegerField(default=10)
    questions = models.ManyToManyField(Question)
    
    
    def __str__(self):
        return self.title
    
    
class History(models.Model):
    history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    quiz_id = models.CharField(max_length=10000,default="")
    score = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.user.username + '  |  ' + self.quiz_id
    