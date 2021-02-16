# pages/urls.py
from django.urls import path
from .views import HomePageView, ResultsPageView

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('results/', ResultsPageView.as_view(), name='results'), # new
]
