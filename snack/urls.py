from django.urls import path

from snack.views import (SnackListView,SnackDetailView,SnackCreateView , SnackUpdateView , SnackDeleteView) 



urlpatterns=[
    path('' , SnackListView.as_view() , name='list_view'),
    path('<int:pk>/' , SnackDetailView.as_view() , name='snack-detail'),
    path('create/' , SnackCreateView.as_view() , name='snack-create'),
    path("<int:pk>/update/", SnackUpdateView.as_view(), name="snack-update"),
     path("<int:pk>/delete/", SnackDeleteView.as_view(), name="snack-delete"),
]