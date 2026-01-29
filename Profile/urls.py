from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('quiz/',views.quiz,name='quiz'),
    path('purpose/',views.purpose,name='purpose'),
    path('received/',views.received,name='received'),
    path('final/',views.final,name='final'),
    path('describe/',views.describe,name='describe'),
    path('question/',views.question,name='question'),
]
