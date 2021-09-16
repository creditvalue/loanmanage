from account.views import addmoney
from django.contrib import admin
from .models import User
from .models import Uhistory,loanapply

# Register your models here.
admin.site.register(User)
admin.site.register(Uhistory)
admin.site.register(loanapply)