from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'textutils.html')

def analyze(request):
    # Get the text from textarea
    text=request.GET.get('text','default')
    lst="~`!@#$%^&*()?></|\{}[]+=_-"

    # Get the text from inputs switches
    uppercaps=request.GET.get('uppercaps','off')
    removepunc=request.GET.get('removepunc','off')
    removenewline=request.GET.get('removenewline','off')
    removeextraspace=request.GET.get('removeextraspace','off')
    purpose=''
    txt=text
    if(uppercaps=="on"):
        txt = txt.upper()
        purpose+="Capitalizing, "


    if(removepunc == "on"):
        str=list(txt)
        for i in range(len(txt)):
            if(txt[i] in lst):
                str.remove(txt[i])
        txt="".join(str)
        purpose+="Removing punctuations, "


    if(removenewline=="on"):
        str=list(txt)
        for i in range(len(txt)):
            if (txt[i]=="\n" or txt[i]=="\r"):
                str.remove(txt[i])
        txt = "".join(str)
        purpose+="Removing new lines, "


    if(removeextraspace=="on"):
        str = list(txt)
        for i in range(len(txt)):
            if (txt[i] == ' '):
                str.remove(txt[i])
        txt = "".join(str)

        purpose += "Removing extra spaces"


    if(uppercaps=="off" and removepunc == "off" and removenewline=="off" and removeextraspace=="off"):
        return HttpResponse("Error!!")

    params = {'purpose':purpose, 'analyzed':txt}
    return render(request,'analyze.html',params)