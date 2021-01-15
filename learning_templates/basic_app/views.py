from django.shortcuts import render

# Create your views here.

def index(request):
    c_dict={"number":25,"word":"my world"}
    return render(request,'basic_app/index.html',c_dict)


def other(request):
    return render(request,'basic_app/other.html')


def relative(request):
    return render(request,'basic_app/relative_url_templates.html')