from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError
from django.shortcuts import render

# Create your views here.


def index(request):
    print(request.GET)
    return HttpResponse('MAIN PAGE')


def catalog(request):
    print(request.GET)
    if request.GET:
        products = request.GET
        return HttpResponse(
            f"<h1>LIST OF GOODS</h1> <p> Type: {products['type']} <p>          "
            f"{products['name']} </p> </p>"
            )
    return HttpResponse('<h1>LIST OF GOODS</h1>')


def good_id(request, good_id):
    return HttpResponse(f'<h1>GOOD № {good_id}</h1>')


def archive(request, year_archive):
    if int(year_archive) < 1990 or int(year_archive) > 2022:
        raise Http404
    return HttpResponse(f'<h2> ARCHIVE: </h2> <p>year {year_archive}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def server_errors(request, exception):
    return HttpResponseServerError('<h1>Сервис недоступен</h1>')
