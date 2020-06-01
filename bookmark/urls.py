from django.urls import path

# 뷰에서 불러올 클래스를 지정
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView


urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    # <int:pk> 와 같은것을 컨버터라고 한다. 기본재공하는 컨버터는 5개(str, int, slug, uuid, path)
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]


#! 컨버터에 대해 알아보자
# str : 문자열 '\'는 제외 컨버터를 사용하지 않을 경우 기본 컨버터
# path : 기본적으로 str과 같은 기능이나 '\'도 포함. url이 아닌 전체에 대한 매칭
# int : 0을 포함한 양의 정수와 매칭 보통 pk(프라이머리키)를 사용한다.
# slug : 아스키 문자나 숫자, 하이픈, 언더스코어를 포함한 슬러그 문자열 매칭
# uuid : uuid와 매칭, 같은페이지에 여러 url이 연결되는 것을 막으려고 사용
