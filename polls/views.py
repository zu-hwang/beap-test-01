# 템플릿 렌더를 위해 임포트 / 단축형404에러 호출
from django.views import generic  # 제너릭 뷰 작성법을 알아보장

"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect  # html 응답을 위한 임포트
from django.urls import reverse
from django.http import Http404  # 404오류 임포트
"""

from .models import Question, Choice  # 데이터베이스 접근을 위한 모델 임포트

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DeatilView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DeleteView):
    model = Question
    template_name = 'polls/results.html'


def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(req, 'polls/detail.html', {'question': qeustion, 'error_message': 'you didnt select a choice.'})
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:reaults', args=(question.id,)))
