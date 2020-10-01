from django.db import models
from django.contrib import admin
import ast 
from django.core import serializers
from django.utils import timezone

# Create your models here.
class Friend(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slate_id = models.CharField(max_length=100, unique = True, default="") 

# exam holds a stringified version of the test for this unique slate_id
# I will probably add a model for grade and grades of subsections
# The grading will happen in Javascript as the exam is taken 
# The grades will be brought in as strings
    # grade = models.CharField(max_length = 3)
    # correct_out_of_all = models.CharField(max_length = 20)
    # correct_out_of_treble = models.CharField(max_length = 20)
    # correct_out_of_bass = models.CharField(max_length = 20)
    # correct_out_of_keyboard = models.CharField(max_length = 20)
    # correct_out_of_rhythm = models.CharField(max_length = 20)
    # correct_out_of_keys = models.CharField(max_length = 20)

    exam = models.JSONField(default=list)
    
    @property
    def question(self):
        return self.exam[1]

    @property 
    def get_slate_id(self):
        return self.slate_id

    @property
    def grade(self):
        current_grade = 0
        out_of = 0
        for i in self.exam[1:]:
            try:
                if i['given_pitch'] == i['answer_pitch'] and i['given_accidental'] == i['answer_accidental']:
                    current_grade += int(i['points_worth'])
                out_of += 1
            except:
                pass
        return str(int(100*current_grade/out_of))+"%"

    @property
    def treble_grade(self):
        current_grade = 0
        out_of = 0
        for i in self.exam[1:]:
            try:
                if i['question_type'][-6:] == 'Treble':
                    if i['given_pitch'] == i['answer_pitch'] and i['given_accidental'] == i['answer_accidental']:
                        current_grade += int(i['points_worth'])
                    out_of += 1
            except:
                pass
        return str(int(100*current_grade/out_of))+"%"


    @property
    def bass_grade(self):        
        current_grade = 0
        out_of = 0
        for i in self.exam[1:]:
            try:
                if i['question_type'][-4:] == 'Bass':
                    if i['given_pitch'] == i['answer_pitch'] and i['given_accidental'] == i['answer_accidental']:
                        current_grade += int(i['points_worth'])
                    out_of += 1
            except:
                pass
        return str(int(100*current_grade/out_of))+"%"

    @property
    def insert_barline_grade(self):
        current_grade = 0
        out_of = 0
        for i in self.exam[1:]:
            try:
                if i['question_type'] == 'Insert_Barlines':
                    if i['given_rhythm'] == i['answer_rhythm']:
                        current_grade += 1
                    out_of += 1
            except: 
                pass
        return str(int(100*current_grade/out_of))+"%"

    def __str__(self):
        return self.first_name + self.last_name

    def quoted_name(self):
        return "'%s'" % self.slate_id






