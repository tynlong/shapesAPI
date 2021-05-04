from django.urls import path,include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from shapeCRUD import views



urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    path('shapes/<shape>/', views.shape_list),
    path('shapes/<shape>/<int:pk>/', views.shape_detail),
    path('shapes/<shape>/<int:pk>/area', views.get_area),
    path('shapes/<shape>/<int:pk>/perimeter', views.get_perimeter),
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetail.as_view()),



]

urlpatterns = format_suffix_patterns(urlpatterns)