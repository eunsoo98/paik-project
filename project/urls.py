from django.contrib import admin
from django.urls import path
import mysite.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mysite.views.index, name='index'),
    path('mysite/blogleftsidebar/', mysite.views.blogleftsidebar, name='blogleftsidebar'),
    path('mysite/activity/', mysite.views.activity, name='activity'),
    path('mysite/education/', mysite.views.education, name='education'),
    path('mysite/finance/', mysite.views.finance, name='finance'),
    path('mysite/translation/', mysite.views.translation, name='translation'),
    path('mysite/travel/', mysite.views.travel, name='travel'),
    path('mysite/welfare/', mysite.views.welfare, name='welfare'),
]
