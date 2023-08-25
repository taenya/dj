#i created this:)
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'index.html')
    #return HttpResponse("HOME")

def analyze(request):
    #get the text 
    djtext=request.POST.get('text','default')
    #checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    
    #when remove punctuation check box is on
    if removepunc=="on":
       punctuations='''/[-[\]{}()*+?.,\\^$|#\]/,!"\\$&"'''
       analysed=""
       for char in djtext:
            if char not in punctuations:
               analysed=analysed+char
       params={'purpose':'remove punctuation','analysed_text':analysed}
       djtext=analysed
        #analyse the text
       #return render(request,'analyze.html',params)
    
    #when caps check box is on
    if(fullcaps=="on"):
        analysed=""
        for char in djtext: 
           analysed=analysed+char.upper()
        params={'purpose':'Changed to Uppercase','analysed_text':analysed}
        djtext=analysed
        #analyse the text
        #return render(request,'analyze.html',params)
     
    if(newlineremover=="on"):
        analysed=""
        for char in djtext: 
           if char !="\n" and char!="\r":
              analysed=analysed+char
        params={'purpose':'Removed newlines','analysed_text':analysed}
        djtext=analysed
        #analyse the text
        #return render(request,'analyze.html',params)
     
    if(spaceremover=="on"):
        analysed=""
        for index,char in enumerate(djtext): 
           if not(djtext[index]==" " and djtext[index+1]==" "):
              analysed=analysed+char
        params={'purpose':'space removed','analysed_text':analysed}
        djtext=analysed
        #analyse the text
        #return render(request,'analyze.html',params)
    #when check box is not on
    #else:
       #return HttpResponse("Error")
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and spaceremover!="on"):
       return HttpResponse("Error")
       
    return render(request,'analyze.html',params)
    
#def capfirst(request):
   # return HttpResponse('''<h1>cap first</h1> <a href="/">Back</a>''')

