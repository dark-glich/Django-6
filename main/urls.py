from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # Home View
    path('', views.HomeView, name='Home'),
    # Maths View
    path('maths', views.MathsView, name='Maths'),
    path('maths/<str:book>', views.MathsChapterView, name='MathsChapter'),
    path('maths/<str:book>/<str:chapter>', views.MathsExerciseView, name='MathsExercise'),
    path('maths/<str:book>/<str:chapter>/<str:exercise>', views.MathsQuestionView, name='MathsQuestion'),
    # Other Subject View
    path('os/<subject>', views.SubjectView, name='Subject'),
    path('os/<str:subject>/<str:chapter>', views.SubjectQuestionView, name='SubjectQuestion')
]
