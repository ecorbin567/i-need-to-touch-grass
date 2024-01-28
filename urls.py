from django.urls import path

from . import views

app_name = "touch_grass"
urlpatterns = [
    # ex: /touch_grass/
    path("", views.index, name="index"),
    # ex: /touch_grass/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /touch_grass/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /touch_grass/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
