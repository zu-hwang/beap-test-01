# 템플릿 렌더를 위해 임포트 / 단축형404에러 호출
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect  # html 응답을 위한 임포트
from django.urls import reverse
# from django.http import Http404  # 404오류 임포트
from .models import Question, reverse  # 데이터베이스 접근을 위한 모델 임포트

# Create your views here.


def index(req):
    # Question 모델의 데이터를 날짜순으로 가져와서 변수에 담는다.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 템플릿을 불러온다
    # 가져온 질문 목록을 , 로 구분하여 이어 붙인뒤 변수에 담는다.
    context = {
        'latest_question_list': latest_question_list,
    }
    # 화면에 출력될 내용을 전달한다.
    # render 매서드를 불러들인뒤 2번째 인자로 템플릿파일을 지정한다.
    # render(응답, '템플릿경로', 템플릿에 전달할 키&값)
    return render(req, 'polls/index.html', context)


def detail(req, question_id):
    """
      try:
          # Question 테이블에 pk가 question_id인 값을 question에 담는다
          question = Question.objects.get(pk=question_id)
      except Question.DoesNotExist:
          # Question 테이블에 pk가 question_id인 값이 존재 하지 않으면 에러 발생시키기
          raise Http404("Question does not exist")  # raise로 에러 발생
    """
    # 위 try & except 방식으로 404 에러를 구현 해도 되지만 아래 숏컷 메서드를 통해 단순하게 구현 할 수 있다!
    question = get_object_or_404(question, pk=question_id)
    return render(req, 'polls/detail.html', {'question': question})


def results(req, question_id):
    question = get_object_or_404(question, pk=question_id)

    return render(req, 'polls/results.html', {'question': question})


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
