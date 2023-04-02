from django.urls import path

from . import views

urlpatterns = [

	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('history/', views.history, name="history"),
	path('send_Request/', views.makeRequest, name="send_Request"),
	path('payment/', views.payment, name="payment"),
	path('Login/', views.Login, name="Login"),







	



]