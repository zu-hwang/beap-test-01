import datetime

from django.db import models  # 장고의 db에게 models를 상속받고 그속 클래스 Model을 상속 받는다
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # 인자로 'date published'로 전달하면 사람이 읽을 수 있는 형태로 전달된다.
    pub_date = models.DateTimeField('date published')

    # 시간계산 메서드 작성 (detetime과 django.utils > timezone 불러오기)
    def was_publiched_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_publiched_recently.admin_order_field = 'pub_date'
    was_publiched_recently.boolean = True
    was_publiched_recently.short_description = 'Published recently?'
    # __str__메서드는 관리자 화면이나 쉘에서 객체를 출력할때 나타날 내용을 결정한다.

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
