from django.db import models
from django.urls import reverse

class Book(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Comments(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    Comment = models.TextField()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Maths(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=156)
    chapter_no = models.IntegerField(default=0)
    exercise = models.CharField(max_length=40)
    question_no = models.IntegerField(default=1)
    question = models.TextField()
    answer = models.TextField()
    
    class Meta:
        verbose_name = 'Maths Question'
        verbose_name_plural = 'Maths Questions'

    def get_absolute_url(self):
        return reverse('main:Maths', kwargs={'book' :self.id})

    def __str__(self):
        return f'chapter = {self.chapter_no} / Exercise = {self.exercise} / Q = {self.question_no}'

class Science(models.Model):
    chapter_name = models.CharField(max_length=156)
    chapter_no = models.IntegerField(default=0)
    question_no = models.IntegerField(default=1)
    question = models.TextField()
    answer = models.TextField()
    
    class Meta:
        verbose_name = 'Science Question'
        verbose_name_plural = 'Science Questions'

    def __str__(self):
        return f'chapter = {self.chapter_no} / Question = {self.question_no}'

class History(models.Model):
    chapter_name = models.CharField(max_length=156)
    chapter_no = models.IntegerField(default=0)
    question_no = models.IntegerField(default=1)
    question = models.TextField()
    answer = models.TextField()
    
    class Meta:
        verbose_name = 'History Question'
        verbose_name_plural = 'History Questions'

    def __str__(self):
        return f'chapter = {self.chapter_no} / Question = {self.question_no}'

class Civics(models.Model):
    chapter_name = models.CharField(max_length=156)
    chapter_no = models.IntegerField(default=0)
    question_no = models.IntegerField(default=1)
    question = models.TextField()
    answer = models.TextField()
    
    class Meta:
        verbose_name = 'Civics Question'
        verbose_name_plural = 'Civics Questions'

    def __str__(self):
        return f'chapter = {self.chapter_no} / Question = {self.question_no}'

class Economics(models.Model):
    chapter_name = models.CharField(max_length=156)
    chapter_no = models.IntegerField(default=0)
    question_no = models.IntegerField(default=1)
    question = models.TextField()
    answer = models.TextField()
    
    class Meta:
        verbose_name = 'Economics Question'
        verbose_name_plural = 'Economics Questions'

    def __str__(self):
        return f'chapter = {self.chapter_no} / Question = {self.question_no}'

class Geography(models.Model):
    chapter_name = models.CharField(max_length=156)
    chapter_no = models.IntegerField(default=0)
    question_no = models.IntegerField(default=1)
    question = models.TextField()
    answer = models.TextField()
    
    class Meta:
        verbose_name = 'Geography Question'
        verbose_name_plural = 'Geography Questions'

    def __str__(self):
        return f'chapter = {self.chapter_no} / Question = {self.question_no}'




