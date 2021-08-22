from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
# Create your views here.
# from django.http import HttpResponse

def index(request):
    '''
    pybo 목록 출력
    '''
    question_list = Question.objects.order_by('-create_date')
    context = {
        'question_list': question_list
    }

    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    # pybo 내용 출력
    question = get_object_or_404(Question, pk = question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    # pybo 답변 등록
    question = get_object_or_404(Question, pk = question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)  # False: DB commit X (임시 저장)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id = question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    # pybo 질문 등록
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)  # False: DB commit X (임시 저장)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form }
    return render(request, 'pybo/question_from.html', context)

