from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    subject = models.CharField(max_length = 200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)  # 이 답변과 연결된 질문(Question)이 삭제될 경우 답변(Answer)도 함께 삭제된다는 의미이다.
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null = True, blank = True)


