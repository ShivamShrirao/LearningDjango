from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
	path('',views.index,name='index'),
	path('homepage/',views.HomepageView.as_view(),name='homepage'),
	path('login/',views.login_request,name='login'),
	path('logout/',views.logout_request,name='logout'),
	path('register/',views.register_request,name='register'),
	path('about/',views.AboutView.as_view(),name='about'),
	path('<int:pk>/',views.DetailView.as_view(),name='detail'),
	path('<int:pk>/results',views.ResultsView.as_view(),name='results'),
	path('<int:question_id>/vote',views.vote,name='vote'),
]