# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from uroquiz.models import Uroquiz
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render_to_response('home.html')


def search(request):
    error = False
    q, yr, ct = "", "", ""
    question_set = Uroquiz.objects.filter()

    if request.GET.get('q'):
        question_set = question_set.filter(question__icontains=q)

    if request.GET.get('yr'):
        question_set = question_set.filter(year=yr)

    if request.GET.get('ct'):
        question_set = question_set.filter(cat__icontains=ct)

    paginator = Paginator(question_set, 1)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        question_set = paginator.page(page)
    except (EmptyPage, InvalidPage):
        question_set = paginator.page(paginator.num_pages)

    return render_to_response('search_results.html',
        {'question': question_set, 'query': q, 'year': yr, 'ct': ct})

def results(request):
    return render_to_response('results.html')

def login(request):
    return render_to_response('login.html')

def register(request):
    return render_to_response('register.html')


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><<td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))