# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from uroquiz.models import Uroquiz
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render_to_response('home.html')


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']

        if not q:
            error = True
        else:
            question_set = Uroquiz.objects.filter(question__icontains=q)
            paginator = Paginator(question_set, 1)
            page = request.GET.get('page')

            try:
                question_set = paginator.page(page)
            except PageNotAnInteger:
                question_set = paginator.page(1)
            except EmptyPage:
                question_set = paginator.page(paginator.num_pages)
            return render_to_response('search_results.html',
                {'question': question_set, 'query': q})
        #yr = request.GET['yr']
        #ct = request.GET['ct']
    return render_to_response('search_form.html', {'error': error})

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