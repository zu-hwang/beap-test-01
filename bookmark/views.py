from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Bookmark  # 북마크 모델 불러오기

# Create your views here.
# 뷰는 엔드포인트를 작성. 프론트에 파일을 어떻게 전달할지 로직을 작성하지요~


# 위코드에서는 ListView 말고 그냥 View를 상속받아 사용했다.
class BookmarkListView(ListView):
    model = Bookmark
    pagenate_by = 3


class BookmarkCreateView(CreateView):
    model = Bookmark

    # field는 인풋으로 받을 데이터베이스의 컬럼을 지정한다.
    fields = ['site_name', 'url']

    # 글쓰기 완료후 이동하게 될 위치 지정 인자 'list'는 urls.py에 지정한 이름 = 북마크 루트 경로로 이동 = 리스트보기
    success_url = reverse_lazy('list')

    # 템플릿 의 접미사를 지정해주었다. bookmark_create라는 이름의 템플릿을 사용하게 된다.
    template_name_suffix = '_create'


class BookmarkDetailView(DetailView):
    model = Bookmark
    template_name_suffix = '_detail'


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
