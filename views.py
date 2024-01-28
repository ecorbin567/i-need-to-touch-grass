from django.http import HttpResponse
from django.shortcuts import render
from .places_information import get_places, places_to_dataframe
from .models import ContactUsForm
import pandas as pd


def index(request):
    places = ['Nothing yet. While you wait, count the squirrels outside your window!']
    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            address = contact_form.cleaned_data['your_street_address']
            keyword = contact_form.cleaned_data['keyword']
            km = contact_form.cleaned_data['maximum_kilometers_away']
            places = get_places(address, keyword, km)
            # df = places_to_dataframe(places)
            # df = df.to_html()
    else:
        # this must be a GET request, so create an empty form
        contact_form = ContactUsForm()
    context = {"form": contact_form, "places": places}
    return render(request, "touch_grass/index.html", context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
