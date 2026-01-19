from django.http import HttpResponse


def reviews_list(request):
    return HttpResponse("views list")