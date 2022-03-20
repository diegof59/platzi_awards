from django.urls import path
from . import views

urlpatterns = [
  path("", views.list, name="polls"),
  path("<int:question_id>/", views.details, name="details"),
  path("<int:id>/vote/", views.vote, name="vote")
]