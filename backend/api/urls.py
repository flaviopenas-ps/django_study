from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.CreateNoteList.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.DeleteNote.as_view(), name="delete-note"),
]