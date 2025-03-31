from django.contrib.auth.models import User
from .forms import SimpleSignUpForm, QuestionForm, AnswerForm
from django.contrib.auth import login
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Question, Answer
from django.db.models import Q


# Create your views here.
@login_required
def search_view(request):
    query = request.GET.get('q', '').strip()
    questions = []
    if query:
        # Filter questions whose title or content contains the query,
        # or whose related answers contain the query.
        questions = Question.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(answers__content__icontains=query)
        ).distinct()

    context = {
        'query': query,
        'questions': questions,
    }
    return render(request, 'connect/search_results.html', context)


@login_required(login_url='login')
def connect_home(request):
    questions = Question.objects.all().order_by('-created_at')

    return render(request, 'connect/home.html', {'questions': questions})


@login_required(login_url='login')
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('connect_home')
        else:
            # If the form is invalid, print the error message for debugging
            print('Error! Form is invalid')
            return render(request, 'connect/ask_question.html', {'form': form})
    else:
        form = QuestionForm()
        return render(request, 'connect/ask_question.html', {'form': form})


@login_required
def answer_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('connect_home')
    else:
        form = AnswerForm()
    return render(request, 'connect/answer_question.html', {'form': form, 'question': question})


def signup_view(request):
    if request.method == 'POST':
        form = SimpleSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'This username is already taken.')
                return render(request, 'connect/signup.html', {'form': form})

            # Create the user and log them in
            user = User.objects.create_user(
                username=username, password=password)
            login(request, user)

            # Pass a success flag to the template
            return render(request, 'connect/signup.html', {'form': form, 'success': True})

        else:
            # If the form is invalid, print the error message for debugging
            print('Error! Form is invalid')
            return render(request, 'connect/signup.html', {'form': form})

    else:
        # If the request method is GET, create an empty form
        form = SimpleSignUpForm()
        return render(request, 'connect/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('connect_home')
        else:
            # Form is not valid: re-render the page with error messages
            return render(request, 'connect/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'connect/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
