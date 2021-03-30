from django.shortcuts import render
from .models import *
from .forms import comments_section
from django.http import Http404
from django.apps import apps
from django.contrib import messages


# Comment Section
def comment_section(request):
    form = comments_section(request.POST or None)
    if form.is_valid():
        messages.success(request, 'Thank You❤️')
        form.save()
        form = comments_section()
    return form


# Main Home View
def HomeView(request):
    # Accessing the comment section
    form = comment_section(request)
    context = {'form':form}
    return render(request, 'home.html', context)


#Books View of Maths
def MathsView(request):
    # Accessing the comment section
    form = comment_section(request)
    books = Book.objects.all()
    return render(request, 'Maths/maths.html', {'books':books, 'form':form})


#Chapter View Page for Maths 
def MathsChapterView(request, book):
    # Accessing the comment section
    form = comment_section(request)
    maths = Maths.objects.filter(book=book)
    book_name = Book.objects.get(id=book)

    # Creating a list of chapters without repeating ChapterNo & ChapterName
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
    return render(request, 'Maths/mathsbook.html', context)


# Exercise View page for Maths
def MathsExerciseView(request, book, chapter):
    form = comment_section(request)
    maths = Maths.objects.filter(book=book, chapter_no=int(chapter))
    book_name = Book.objects.get(id=book)

    # Creating a list a exercises without repeating
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
    return render(request, 'Maths/mathsexercise.html', context)


# View for question answers page of Maths
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
    return render(request, 'Maths/mathsquestions.html', context)


# Chapter View page of other subjects
def SubjectView(request, subject):
    # Accessing the comment section
    form = comment_section(request)
    # Getting model subject with string subject
    Model = apps.get_model('main', subject)
    sub = Model.objects.all()

    # Creating a list of chapters without repeating ChapterNo & ChapterName
    chapters = []
    for i in sub:
        if {
            'ChapterNo':i.chapter_no ,
            'ChapterName':i.chapter_name
            } not in chapters:
            chapters.append({'ChapterNo':i.chapter_no, 'ChapterName':i.chapter_name})
        else:
            pass

    context = {
        'chapters':chapters,
        'form':form,
        'subject': subject
    }
    return render(request, 'Other_Subjects/subject.html', context)


# View for question answers page of other subjects
def SubjectQuestionView(request, subject, chapter):
    # Accessing the comment section
    form = comment_section(request)
    # Getting model subject with string subject
    Model = apps.get_model('main', subject)
    sub = Model.objects.all()

    context = {
        'form':form,
        'questions': sub,
        'subject':subject,
        'chapter':chapter
    }
    return render(request, 'Other_Subjects/SubjectQuestion.html', context)
