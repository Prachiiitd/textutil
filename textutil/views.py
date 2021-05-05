# i have created this file
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<a href="https://www.google.com/search?q=www.facebook+login.com&rlz=1C1SQJL_enIN895IN896&oq=www.fa&aqs=chrome.1.69i57j0i131i433j0i433j0i131i433j0i271j5j5i44l2.5635j0j15&sourceid=chrome&ie=UTF-8">Facebook login</a>''')
# def about(request):
#     return HttpResponse("Hello about")
def index(request):
    # p={"name":"harry","place":"mars"}
    # return render(request,'index.html',p)
    # return HttpResponse("Home")
    return render(request, 'index.html')

def analyze(request):
    # get the text analize the text
    djtext=request.POST.get('text',"default")
    # print(djtext)
    fullcap=request.POST.get("fullcaps","off")
    # print(fullcaps)
    rpunc = request.POST.get("removepunc", "off")
    newlineremove=request.POST.get("newlineremover","off")
    extraspace=request.POST.get("spaceremover","off")
    # print(rpunc)
    # analyzed=djtext
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if rpunc=="on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        p={"purpose":"remove punctuations","analyzed_text":analyzed}
        djtext=analyzed
        # return render(request,"analyze.html",p)
    if fullcap=="on":
        analyzed=djtext.upper()
        p = {"purpose": "Change to upper case", "analyzed_text": analyzed}
        djtext=analyzed
        # return render(request,"analyze.html",p)
    if newlineremove=="on":
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed+=char
        p={"purpose":"remove new line","analyzed_text":analyzed}
        djtext=analyzed
        # return render(request,"analyze.html",p)
    if extraspace=="on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed += char
        p = {"purpose": "remove new line", "analyzed_text": analyzed}
        djtext=analyzed
        # return render(request, "analyze.html", p)
    if  rpunc=="on" or fullcap=="on" or newlineremove=="on" or extraspace=="on":
        return render(request,"analyze.html",p)

    else:
        return HttpResponse("Error")
# def capfirst(request):
#     return HttpResponse("capitalise first")
# def newlineremove(request):
#     return HttpResponse("new line remove")
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'> back</a>")
# #will return bacck to home page
# def charcount(request):
#     return HttpResponse("char count")
# def capfirst(request):
#     return HttpResponse("capitalise first")
