# In quiz_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, QuizTaker, Question, Choice, UserAnswer

@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_app/quiz_list.html', {'quizzes': quizzes})

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quiz_app/quiz_detail.html', {'quiz': quiz})

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    if request.method == 'POST':
        user_quiz_taker = QuizTaker.objects.create(user=request.user, quiz=quiz, score=0.0)
        score = 0.0
        for question in questions:
            selected_choice_id = request.POST.get(f'choice_{question.id}')
            if selected_choice_id:
                selected_choice = get_object_or_404(Choice, id=selected_choice_id)
                UserAnswer.objects.create(quiz_taker=user_quiz_taker, question=question, choice=selected_choice)
                if selected_choice.is_correct:
                    score += 1.0
        user_quiz_taker.score = (score / len(questions)) * 100.0
        user_quiz_taker.save()
        return redirect('quiz_app:quiz_result', quiz_id=quiz_id, quiz_taker_id=user_quiz_taker.id)
    return render(request, 'quiz_app/take_quiz.html', {'quiz': quiz, 'questions': questions})

@login_required
def quiz_result(request, quiz_id, quiz_taker_id):
    quiz_taker = get_object_or_404(QuizTaker, id=quiz_taker_id)
    return render(request, 'quiz_app/quiz_result.html', {'quiz_taker': quiz_taker})

@login_required
def leaderboard(request, quiz_id):
    quiz_takers = QuizTaker.objects.filter(quiz_id=quiz_id).order_by('-score')
    return render(request, 'quiz_app/leaderboard.html', {'quiz_takers': quiz_takers})
