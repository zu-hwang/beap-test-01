"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# include는 다른 urls.py를 참조할 수 있도록 한다.
# xxx.com/polls/SSS 라고 했을때 ~~~~/polls/ 까지는 메인 Urls.py에서 찾고
# 나머지는 include에 지정한 경로 파일에서 sss 를 찾는다.

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('admin/', admin.site.urls),
]
