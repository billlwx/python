# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from MysqldbHelper import *

# Create your views here.
def index(request):

    return render_to_response('index.html')

def tools(request):

    return render_to_response('tools.html')

def single(request):

    return render_to_response('single.html')


def autoreport(request):

    return render_to_response('reportlist.html')




