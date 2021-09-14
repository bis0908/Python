from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views.generic import ListView
# Create your views here.
# from django.http import HttpResponse

def index(request):
    # pybo 목록 출력
    # 입력 파라미터
    page = request.GET.get('page', '1')

    # 조회
    question_list = Question.objects.order_by('-create_date')
    # 페이징 처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = { 'question_list': page_obj }

    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    # pybo 내용 출력
    question = get_object_or_404(Question, pk = question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url = 'common:login')
def answer_create(request, question_id):
    # pybo 답변 등록
    question = get_object_or_404(Question, pk = question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)  # False: DB commit X (임시 저장)
            answer.author = request.user # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id = question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url = 'common:login')
def question_create(request):
    # pybo 질문 등록
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)  # False: DB commit X (임시 저장)
            question.author = request.user # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form }
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url = 'common:login')
def question_modify(request, question_id):
    # pybo 질문 수정 기능
    question = get_object_or_404(Question, pk = question_id)
    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다')  # messeges 모듈을 이용해 오류 발생 시키기. (로그인 유저 != 글쓴이)
        return redirect('pybo:detail', question_id = question.id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance = question)
        if form.is_valid():
            question = form.save(commit = False)
            question.modify_date = timezone.now() # 수정일자 저장 (현재 일시로)
            question.save()
            return redirect('pybo:detail', question_id = question.id)
    else:
        form = QuestionForm(instance = question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)