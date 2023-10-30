from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError
from django.shortcuts import render
from django.template.loader import render_to_string


# Create your views here.
storage_lst = [
    {'id': 1, 'title': 'Склад_Москва', 'address': 'Мкад 2 км', 'open': True},
    {'id': 2, 'title': 'Склад_Химки', 'address': 'Мега Химки', 'open': True},
    {'id': 3, 'title': 'Склад_Красногорск', 'address': 'Павшино', 'open': True},
    {'id': 4, 'title': 'Склад_Одинцово', 'address': 'Можайское шоссе', 'open': False},
    {'id': 5, 'title': 'Склад_Мытищи', 'address': 'Колпакова', 'open': True}
    ]
main_menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти / Зарегистрироваться', 'url_name': 'log_in'}
    ]

def index(request):
    title = "Список складов"
    data = {'storages': storage_lst, 'title': title, 'menu': main_menu}
    return render(request, 'store/index.html', context=data)


def contact(request):
    return HttpResponse('Форма обратной связи')


def log_in(request):
    return HttpResponse('Регистрация')


def show_store(request, store_id):
    return HttpResponse(f'Склад {store_id}')


def about(request):
    data = {"title": "информация о сайте"}
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
