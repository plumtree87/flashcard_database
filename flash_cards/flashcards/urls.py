from django.urls import path
from . import views

urlpatterns = [
    path('flashcards/', views.CardList.as_view()),
    path('collection/', views.CollectionList.as_view()),
    path('flashcards/<int:fk>/', views.CardDetail.as_view()),
    path('collection/<int:pk>/', views.CollectionList.as_view()),
    path('single/<int:pk>/', views.CollectionSingle.as_view()),
]