from django.urls import path
from . import views
from .views import counter
from .views import bus
from .views import payment
#from .views import profile

urlpatterns = [
    path('', views.home, name="home"),
    path('findbus', views.findbus, name="findbus"),
    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),
    path('counter',counter.as_view(), name='counter'),
    path('bus',bus.as_view(), name='bus'),
    path('payment',views.payment, name='payment')
    #path('profile', views.profile, name='profile')
]
