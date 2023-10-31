from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from store.models import Store


main_menu = [
    {'title': 'На главную', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'log_in'}
    ]


def index(request):
    storage_lst = Store.objects.all()
    print(storage_lst)
    data = {'page_title': "Список складов", 'storages': storage_lst, 'menu': main_menu}
    return render(request, 'store/index.html', context=data)


def contact(request):
    return HttpResponse('Форма обратной связи')


def log_in(request):
    return HttpResponse('Регистрация')


def show_store(request, store_slug):
    store = get_object_or_404(Store, store_slug=store_slug)
    data = {'page_title': store.title, 'store': store, 'menu': main_menu}
    return render(request, 'store/store.html', context=data)


def about(request):
    data = {"page_title": "информация о сайте", 'menu': main_menu}
    return render(request, 'store/about.html', context=data)


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


#def server_errors(exception):
#    return HttpResponseServerError('<h1>Сервис недоступен</h1>')
