from django.urls import path
from . import views

urlpatterns = [
  path("", views.List.as_view(), name="polls"),
  path("<int:pk>/", views.Details.as_view(), name="details"),
  path("<int:question_id>/vote/", views.vote, name="vote"),
  path("<int:pk>/results/", views.Results.as_view(), name="results"),
]