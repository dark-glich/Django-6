from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomeView, name='Home'),
    path('maths', views.MathsView, name='Maths'),
    path('os/<subject>', views.SubjectView, name='Subject'),
    path('os/<str:subject>/<str:chapter>', views.SubjectChapter, name='SubjectQuestion'),
    path('maths/<str:book>', views.FilterMathsView, name='MathsChapter'),
    path('maths/<str:book>/<str:chapter>', views.MathsExerciseView, name='MathsExercise'),
    path('maths/<str:book>/<str:chapter>/<str:exercise>', views.MathsQuestionView, name='MathsQuestion')
]
