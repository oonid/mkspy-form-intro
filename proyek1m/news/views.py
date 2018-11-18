from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import modelform_factory
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt  # THIS IS TEMPORARY, to allow form POST

from .forms import NameForm
from .models import Friend

# Create your views here.


def index(request):
    return HttpResponse('Hello, World!')


@csrf_exempt  # this is temporary, to allow form POST, NOT SECURE, remove this later
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.info(request, 'hello {}'.format(form.cleaned_data['your_name']))
            return HttpResponseRedirect('/news/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


@csrf_exempt  # this is temporary, to allow form POST, NOT SECURE, remove this later
def friend_data_form(request):

    # generate FriendForm from model with factory, don't need to manually create FriendForm on forms.py or models.py
    FriendForm = modelform_factory(Friend, fields=('name', 'age', 'sex'))

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FriendForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            # save data to database, save form directly save data to database via ModelForm
            form.save()

            # send django messages
            messages.info(request, 'new friend {} ({}/{})'
                          .format(form.cleaned_data['name'], form.cleaned_data['sex'], form.cleaned_data['age']))

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('friend-form'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FriendForm()

    friends = Friend.objects.all()  # query all data form table, equal with SELECT * FROM friend
    for f in friends:
        print(f)

    return render(request,
                  template_name='friend.html',
                  context={'form': form, 'friends': friends})
