from django.urls import path
from . import views

# 네임스페이스 만들기
app_name = 'polls'

urlpatterns = [
    # path(route, view, kwargs, name)
    # route : 엔트포인트 경로
    # view : 루트로 접근했을때 실행할 views.py의 뷰
    # kwargs : 뷰에 전달할 값들
    # name : route의 이름
    # urls.py를 작성한뒤 루트 urls.py에 추가 > setting.py에 앱추가 까지 해야 한다.

    #! 클래스로 view를 작성했다면 .as_view()메서드를 꼭 적어주어여한다!
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DeatilView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]

"""
    # <int:변수명> : 변수를 적용할 수 있다.
    path('', views.index, name='index'),  # /polls/
    path('<int:question_id>/', views.detail, name='detail'),  # /polls/5/
    path('<int:question_id>/results', views.results,
         name='results'),  # /polls/5/results/
    path('<int:question_id>/vote', views.vote, name='vote'),  # /polls/5/vote/
"""
