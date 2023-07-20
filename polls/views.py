from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Choice, Question, UserResponse
from .utils import random_question

@login_required
def index(request):
    question = random_question(request.user)
    context = {'question': question, 'all_answered': False}
    if question is None:
        context['all_answered'] = Question.objects.all().count() > 0
    return render(request, 'polls/index.html', context)

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        text_answer = request.POST.get('textspace', '')  # Get the text answer from the form
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/index.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        UserResponse.objects.create(
            user=request.user,
            choice=selected_choice,
            question=question,
            text_answer=text_answer,  # Save the text answer in the UserResponse
        )
        return redirect('polls:index')

@login_required
def new_guest_session(request):
    request.session.clear()
    return redirect('polls:index')

@login_required
def results(request):
    user_responses = UserResponse.objects.filter(user=request.user)
    return render(request, 'polls/results.html', {'user_responses': user_responses})
