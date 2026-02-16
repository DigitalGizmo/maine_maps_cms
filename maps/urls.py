from django.urls import path
from . import views

urlpatterns = [
    path('maps/', views.MapSetList.as_view(), name='mapset-list'),
    path('maps/<slug:slug>/', views.MapSetDetail.as_view(), name='mapset-detail'),
]
