from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class User(AbstractUser):
    
    class Meta:
        #IU staff - they need access to only certain students
        #Content creators - need access to content dashboard
        #Students - need access to pupil dashboard
        #Teachers - need access to approval dashboard
        
        permissions = (

            ''
        )

class Content(models.Model):
    FORMAT_TYPES = [
        # ('F', 'Flashcards'),
        # TODO - Add Flashcards, JSON from quill rich text editor and mindmaps
        ('WD', 'Word Document'),
        ('GD', 'Google Docs'),
        ('GS', 'Google Slides')
    ]
    format = models.CharField(
        max_length=2,
        choices=FORMAT_TYPES,
        default='WD'
    )
    subject = models.ForeignKey(
        'Subject',
        on_delete = models.PROTECT,
        related_name='content'
    )

class Subject(models.Model):
    OPTIONS = [
    ('Revision Help', (
        ('RP', 'Revision Plans'),
        ('RT', 'Revision Tips'),
        ('ME', 'Mentors'),
    )),
    ('Subjects', (
        # First three letters of word, or intials of word if more than one (RPH)
        ('BIO', 'Biology'),
        ('CHE', 'Chemistry'),
        ('ENG', 'English'),
        ('ECO', 'Economics'),
        ('FRE', 'French'),
        ('GEO', 'Geography'),
        ('GER', 'German'),
        ('HIS', 'History'),
        ('MAT', 'Maths'),
        ('PHY', 'Physics'),
        ('RPH', 'Religion & Philosophy'),
        ('SPA', 'Spanish')
    )),
    ('Revision Motivation', (
        ('MH', 'Mental Health'),
        ('MG', 'Model GCSE'),
        ('TI', 'Time')
    ))
]
    subject = models.CharField(
        max_length=3,
        choices=OPTIONS,
    )