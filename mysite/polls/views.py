from django.http import HttpResponse
from .models import Question
from django.template import loader


def index(request):
    # pub_date를 최신순으로 정렬하여 latest_qustion_list로 넘겨줌
    latest_question_list = Question.objects.order_by('-pub_data')[:5]
    # join 함수를 통해 output 문자열로 합침
    # output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    # http리퀘스트가 오면 response로 위의 메세지 반환


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
