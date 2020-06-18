from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
# from django.contrib.staticfiles.templatetags.staticfiles import static
# from django.templatetags.static import static
from django.conf.urls.static import static
# from django.templatetags.static import static

from django.http import HttpResponse, JsonResponse, QueryDict
from django.db.models import Value as V
from django.views.generic import CreateView
from xlrd import open_workbook
import pandas as pd
from pandas import ExcelWriter
from django.forms.models import model_to_dict
from pandas import ExcelFile
import time
from django.views import View
from django.http import HttpResponseRedirect
from django.core.mail.backends.smtp import EmailBackend
from django.shortcuts import render
from django.core import serializers
import requests
# import smtplib, urllib3,icalendar, pytz, email, requests, json, csv, re,
# datetime, string, random
from itertools import chain
import matplotlib.pyplot as plt; 

import numpy as np
import ast
from string import punctuation
from django.template import loader
# import os, json, docx2txt, re, nltk, PyPDF2
import re
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from random import randint
# from docx import Document
from django.db.models import Avg, Count, Sum, Q
from django.core.files.storage import default_storage, Storage
from django.core.files.uploadedfile import UploadedFile
# from fpdf import FPDF 
# import fpdf
# import pdfkit, shutil
from rest_framework import status, views, generics, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.http import FileResponse , Http404
from django.contrib.auth.models import User, Group, Permission
from .models import *
from datetime import date
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from io import StringIO
# from pdfminer.layout import LAParams
from django.core.mail import EmailMultiAlternatives, send_mail
from django.utils.html import strip_tags
from django.template import RequestContext
# from .sentiment import generateResults
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import smtplib, urllib3, pytz, email, requests, json, csv, re,  datetime, string, random, os
# icalendar,
from django.db.models.functions import Concat  

from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication
from django.shortcuts import redirect

# from .serializers import CandidateSerializer
# from .views import *
# from docx import Document
# from nltk.tokenize import word_tokenize,sent_tokenize
# from nltk import pos_tag
# from nltk.chunk import ne_chunk
# import datetime as dt
# from nltk.corpus import stopwords
# from string import punctuation
# from pdfminer.converter import TextConverter
# from pdfminer.pdfpage import PDFPage







class LoginView(views.APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        if request.user.id is not None:
            return Response('logged_in')

        return Response()


    def post(self, request):
        username=request.data['username']
        user = authenticate(username=username,password=request.data['password'])
        if  user is not None:
            login(request, user)
            return HttpResponse('logged_in')
        else:
            try:
                user = User.objects.get(username=username)
                return HttpResponse('Password is incorrect', status=400)
            except:
                return HttpResponse('Invalid User ID', status=400)
        
        return Response()



class ProfileView(views.APIView):
    def get(self,request):

        context = {}
        allusers =  User.objects.exclude(id = request.user.id)
        context['users'] = allusers


        return render (request,'profile.html',context)



class DeleteUser(views.APIView):
    def post(self,request):
        try:
            data = request.data
            user = User.objects.filter(id = request.data['userid'])
            user.delete()


            return JsonResponse({'deleted':True})

        except Exception as e:
        
            return JsonResponse({'deleted':False})
class Signupview(views.APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        context = {}
        allusers = User.objects.all()
        userlist = []
        for i in allusers:
            userlist.append(i.username)
        
        context['users'] = json.dumps(userlist)



        return render(request,'signup.html',context)


    def post(self,request):

        try:
            user = User.objects.create(username= request.data['username'])
            user.set_password(request.data['password'])
            user.is_staff = True
            user.save()


            return JsonResponse({'createduser':True})

        except Exception as e:
        
            return JsonResponse({'createduser':False})


class LogoutView(views.APIView):
    def get(self, request):
        logout(request)
        response = redirect('../../')
        return response
       