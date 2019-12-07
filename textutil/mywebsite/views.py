#Aasif created this application
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def analyze(request):
	djtext = request.POST.get('text','default')
	removepunc = request.POST.get('removepunc','off')
	fullcaps = request.POST.get('fullcaps','off')
	newline = request.POST.get('newline','off')
	exspace = request.POST.get('exspace','off')
	charcount = request.POST.get('charcount','off')

	if removepunc == "on":
		punctuations = '''!()-[]{;}:'",<>\./?@#$%^&*_`~'''
		analyzed = ""
		for char in djtext:
			if char not in punctuations:
				analyzed = analyzed + char
		params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
		djtext = analyzed

	if fullcaps == "on":
		analyzed = ""
		for char in djtext:
			analyzed = analyzed + char.upper()
		params = {'purpose':'Change to upper case', 'analyzed_text':analyzed}
		djtext = analyzed

	if newline == "on":
		analyzed = ""
		for char in djtext:
			if char != "\n" and char != "\r":
				analyzed = analyzed + char
		params = {'purpose':'Remove new line', 'analyzed_text':analyzed}
		djtext = analyzed
	if exspace == "on":

		analyzed = ""
		for index, char in enumerate(djtext):
			if not(djtext[index] == " " and djtext[index+1] == " "):
				analyzed = analyzed + char
		params = {'purpose':'Remove extra spaces', 'analyzed_text':analyzed}
		djtext = analyzed

	if charcount == "on":
		analyzed = ""
		analyzed = len(djtext)
		params = {'purpose':'Count character', 'analyzed_text':analyzed}
		djtext = analyzed
		
	if  removepunc != "on" and fullcaps != "on" and newline != "on" and exspace != "on" and charcount != "on" and charcount != "on":
		return HttpResponse("<h1 style = color:red>*******Error*******</h1><br><h3>To avoid this error <a href='/''>click here</a> and select the operations you want...</h3><br>")

	return render(request, 'analyze.html', params)