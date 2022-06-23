from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date published')
    # Question 모델안에 질문 내용과 발행 날짜가 들어있음

    def __str__(self):
        return self.question_text  # 출력 형식 변경


class Choice(models.Model):
    # 외래키로 연결, 질문이 지워질 경우 cascade하게 선택도 지워지도록
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# application의 모델도 프로젝트 모델 스키마에 연결이 필요함
