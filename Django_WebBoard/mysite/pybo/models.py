from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length = 200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)  # 이 답변과 연결된 질문(Question)이 삭제될 경우 답변(Answer)도 함께 삭제된다는 의미이다.
    content = models.TextField()
    create_date = models.DateTimeField()


