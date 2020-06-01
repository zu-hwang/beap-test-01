from django.contrib import admin

# 현재 같은 위치의 models.py파일 내에서 Bookmark 를 불러온다.
from .models import Bookmark

# Register your models here.


# 아래 명령을 통해 Bookmark 모델을 관리할 수 있게 된다.
admin.site.register(Bookmark)
