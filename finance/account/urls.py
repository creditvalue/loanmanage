from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('u_profile/',views.u_profile,name="u_profile"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('addmoney/',views.addmoney,name="addmoney"),
    path('sendmon/',views.sendmon,name="sendmon"),
    path('history/',views.history,name="history"),
    path('checkpoint/',views.checkpoint,name="checkpoint"),
    path('checkpoint/',views.checkpoint,name='checkpoint'),
    # path('udateimage/',views.udateimage,name="udateimage"),
    path('applyloan/',views.applyloan,name="applyloan"),
]
