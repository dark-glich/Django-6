from django.shortcuts import render
from .models import *
from .forms import comments_section
from django.http import Http404
from django.contrib import messages

def comment_section(request):
    form = comments_section(request.POST or None)
    if form.is_valid():
        messages.success(request, 'Thank You❤️')
        form.save()
        form = comments_section()
    return form

def HomeView(request):
    form = comment_section(request)
    context = {'form':form}
    return render(request, 'home.html', context)

def MathsView(request):
    form = comment_section(request)
    books = Book.objects.all()
    return render(request, 'maths.html', {'books':books, 'form':form})

def FilterMathsView(request, book):
    form = comment_section(request)
    maths = Maths.objects.filter(book=book)
    book_name = Book.objects.get(id=book)
    chapters = []
    for mathbook in maths.all():
        if {"number":mathbook.chapter_no, "name":mathbook.chapter_name} not in chapters:
            chapters.append({"number":mathbook.chapter_no, "name":mathbook.chapter_name})
    context = {
        'book':book,
        'maths':maths,
        'form':form, 
        'book_name':book_name.name,
        'chapters': chapters,
    }
    return render(request, 'mathsbook.html', context)

def MathsExerciseView(request, book, chapter):
    form = comment_section(request)
    maths = Maths.objects.filter(book=book, chapter_no=int(chapter))
    book_name = Book.objects.get(id=book)
    exercise = []
    for mathbook in maths.all():
        if mathbook.exercise not in exercise:
            exercise.append(mathbook.exercise)
    context = {
        'maths':maths,
        'book':book,
        'chapter':chapter,
        'form':form, 
        'book_name':book_name.name,
        'exercise': exercise,
    }
    return render(request, 'mathsexercise.html', context)

def MathsQuestionView(request, book, chapter, exercise):
    form = comment_section(request)
    book_name = Book.objects.get(id=book)
    questions = Maths.objects.filter(book=book, chapter_no=int(chapter), exercise=exercise)
    context = {
        'book':book,
        'form':form, 
        'book_name': book_name.name,
        'questions': questions,
        'exercise':exercise,
        'chapter':chapter
    }
    return render(request, 'mathsquestions.html', context)

def SubjectView(request, subject):
    form = comment_section(request)
    sub_list = ['Science', 'History', 'Civics', 'Geography', 'Economics']
    if subject in sub_list:
        if subject == 'Science':
            sub = Science.objects.all()
            sub_name = 'Science'

        if subject == 'History':
            sub = History.objects.all()
            sub_name = 'History'

        if subject == 'Civics':
            sub = Civics.objects.all()
            sub_name = 'Civics'

        if subject == 'Geography':
            sub = Geography.objects.all()
            sub_name = 'Geography'

        if subject == 'Economics':
            sub = Economics.objects.all()
            sub_name = 'Economics'
    else:
        raise Http404

    chapters = []
    for i in sub:
        if {'ChapterNo':i.chapter_no, 'ChapterName':i.chapter_name} not in chapters:
            chapters.append({'ChapterNo':i.chapter_no, 'ChapterName':i.chapter_name})
        
    context = {
        'chapters':chapters,
        'form':form,
        'subject':sub_name
    }
    return render(request, 'Other_Subjects/subject.html', context)

def SubjectChapter(request, subject, chapter):
    form = comment_section(request)
    sub_list = ['Science', 'History', 'Civics', 'Geography', 'Economics']
    if subject in sub_list:
        if subject == 'Science':
            sub = Science.objects.filter(chapter_no=chapter)
        
        if subject == 'History':
            sub = History.objects.filter(chapter_no=chapter)

        if subject == 'Civics':
            sub = Civics.objects.filter(chapter_no=chapter)

        if subject == 'Geography':
            sub = Geography.objects.filter(chapter_no=chapter)
            
        if subject == 'Economics':
            sub = Economics.objects.filter(chapter_no=chapter)
            
    else:
        raise Http404

    context = {
        'form':form,
        'questions': sub,
        'subject':subject,
        'chapter':chapter
        }
    return render(request, 'Other_Subjects/SubjectQuestion.html', context)
