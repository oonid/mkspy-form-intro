from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt  # THIS IS TEMPORARY, to allow form POST

from .forms import NameForm

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
