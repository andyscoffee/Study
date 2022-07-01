from django.http import Http404, HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render


def index(request):
    # pub_date를 최신순으로 정렬하여 latest_qustion_list로 넘겨줌
    # 5. latest~가 유효하다면 index.html의{% for question in ~}코드 수행
    latest_question_list = Question.objects.order_by('-pub_data')[:5]
    """join 함수를 통해 output 문자열로 합침
    output = ', '.join([q.question_text for q in latest_question_list])"""
    # 1. view.py에서 index.html을 로드
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }  # 2. view에서 model의 Question 데이터를 추출한 뒤 context 딕셔너리에 담음
    # 3. 템플릿을 rendering할 때 context에서 데이터를 실어담아 템플릿에 보냄
    return HttpResponse(template.render(context, request))


    # 4. 템플릿은 context에 담긴 내용을 기반으로 html코드를 파이썬으로 작성
"""
render wrapping 함수를 이용한 간단하게 표기한 방법
def index(request):
    latest_question_list = Question.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
"""


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
