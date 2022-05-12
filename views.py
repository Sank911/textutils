from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    widespaceremover = request.POST.get('widespaceremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-+;'.,/'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'removed punctuations', 'analyzed_text': analyzed}
        #   return render(request,'analyze.html',params)
        djtext = analyzed

    if uppercase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Change to upper case', 'analyzed_text': analyzed}
        # return render(request,'analyze.html',params)
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'new line removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if widespaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'extra widespace removed', 'analyzed_text': analyzed}

    if removepunc != "on" and widespaceremover != "on" and newlineremover != "on" and uppercase != "on":
        return HttpResponse("Please select analyzer and try again")

    return render(request, 'analyze.html', params)
