from django.db import models
from django.urls import reverse
# Create your models here.


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        # 객체를 출력할 때 나타낼 값
        return "이름 : " + self.site_name+" / 주소 : " + self.url

    def get_absolute_url(self):
        # 장고에서는 리다이렉션 하기위해 success_url속성 또는 get_absolute_url이라는 메서드를 찾아 지정 경로로 이동하게 된다. success_url 속성은 view에 작성하며 get_absolute_rul메서드는 models에 작성하게 된다.
        return reverse('detail', args=[str(self.id)])
