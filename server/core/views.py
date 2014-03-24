from django.http import HttpResponse

def index(request):
    output = "hello world!"
    return HttpResponse(output)
