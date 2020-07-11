from django.urls import path,re_path
from myapp import views

app_name="myapp"
urlpatterns = [
    path('list/',views.SchoolListView.as_view(),name="list"),
    re_path('^update/(?P<pk>\d+)/',views.SchoolUpdateView.as_view(),name="update"),
    re_path('^delete/(?P<pk>\d+)/',views.SchoolDeleteView.as_view(),name="delete"),
    re_path('(?P<pk>\d+)/',views.SchoolDetailView.as_view(),name="detail"),
    path('create/',views.SchoolCreateView.as_view(),name="create"),
    
]
