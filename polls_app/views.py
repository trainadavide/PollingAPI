from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from polls_app.serializer import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from .forms import PollForm, OptionFormSet

from .models import Poll, Option, User
from django.http import JsonResponse


class PollCreateView(generics.CreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]

class ResponseCreateView(generics.CreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]

class PollResultsView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('Dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'Register.html', {'form': form})


def dashboard(request):
    polls = Poll.objects.all()
    return render(request, 'Dashboard.html', {'polls': polls})

def create_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        formset = OptionFormSet(request.POST, prefix='options')
        if form.is_valid() and formset.is_valid():
            poll = form.save(commit=False)
            poll.user = request.user
            poll.save()

            for form in formset:
                if form.cleaned_data.get('text'):
                    option = form.save(commit=False)
                    option.poll = poll
                    option.save()

            return redirect('Dashboard')
        else:
            print("Form is invalid")
            print("Form.errors: ", form.errors)
            print("Formset.errors: ", formset.errors)
    else:
        form = PollForm()
        formset = OptionFormSet(prefix='options')
    return render(request, 'Poll_Creation.html', {'form': form, 'formset': formset})

def vote(request, poll_id, option_id):
    if request.method == 'POST':
        option = Option.objects.get(id=option_id)
        option.votes += 1
        option.save()

        poll = Poll.objects.get(id=poll_id)

        poll.responded_users.add(request.user)
        poll.save()

        return redirect('Dashboard')

def Delete_poll(request, poll_id):
    if request.method == 'POST':
        poll = Poll.objects.get(id=poll_id)
        if request.user == poll.user:
            poll.delete()
        return redirect('Dashboard')

def UserPolls(request, user_id):
    selected_user = User.objects.get(id=user_id)
    user_polls = Poll.objects.filter(user_id=user_id)
    return render(request, 'User.html', {'selected_user': selected_user, 'user_polls': user_polls})