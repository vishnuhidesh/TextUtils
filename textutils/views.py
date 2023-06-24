# This views file was created by me - Vishnu

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    if removepunc == 'on':
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punc:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed, 'message_title':'Yay!' ,'message':"We have successfully removed the punctuations"}
        return render(request, 'analyze.html', params)

    else:
        params={'purpose':' Not Removed Punctuations','analyzed_text':djtext,'message_title':'Sorry!' ,'message':"None of the options selected"}
        return render(request, 'analyze.html', params)

