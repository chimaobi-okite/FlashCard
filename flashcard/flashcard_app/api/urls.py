from django.urls import path
from flashcard_app.api.views import CardsList, CardDetail

urlpatterns = [
    path("list/", CardsList.as_view(), name='cards-list'),
    path("<int:pk>/", CardDetail.as_view(), name='card-detail'),
]