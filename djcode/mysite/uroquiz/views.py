# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from uroquiz.models import Uroquiz
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from django.template import RequestContext


def home(request):
    return render_to_response('home.html')


def search(request):
    q = request.GET.get('q', '')
    yr = request.GET.get('yr', '')
    ct = request.GET.get('ct', '')
    question_set = Uroquiz.objects.all()

    if q:
        if not (yr or ct):
            question_set = Uroquiz.objects.filter(question__icontains=q)

    if yr:
        if not (q or ct):
            question_set = Uroquiz.objects.filter(year=yr)

    if ct:
        if not (q or yr):
            question_set = Uroquiz.objects.filter(cat__icontains=ct)

    if (q and yr):
        if not ct:
            question_set = Uroquiz.objects.filter(question__icontains=q).filter(year=yr)

    if (q and ct):
        if not yr:
            question_set = Uroquiz.objects.filter(question__icontains=q).filter(cat__icontains=ct)
    if (yr and ct):
        if not q:
            question_set = Uroquiz.objects.filter(year=yr).filter(cat__icontains=ct)
    if ((q and yr) and ct):
        question_set = Uroquiz.objects.filter(question__icontains=q).filter(year=yr).filter(cat__icontains=ct)
    if not ((q or yr) or ct):
            return render_to_response('search_form.html')
    paginator = Paginator(question_set, 1)
    page = request.GET.get('page')
    try:
        question_set = paginator.page(page)
    except PageNotAnInteger:
        question_set = paginator.page(1)
    except EmptyPage:
        question_set = paginator.page(paginator.num_pages)
    return render_to_response('search_results.html',
        {'question': question_set, 'q': q, 'yr': yr, 'ct': ct}, context_instance=RequestContext(request))


def results(request):
    return render_to_response('results.html')

# def login_view(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user is marked "active":
#         # orrect password and user is marked "active"
#         auth.login(required, user)
#         # redirect to succes page
#         return HttpResponseRedirect("/account/loggedin/")
#     else:
#         #show error page
#         return HttpResponseRedirect("/account/invalid/")

# def logout_view(request):
#     auth.logout(request)
#     #redirect to a success page
#     return HttpResponseRedirect("/account/loggedout/")

def loggedout(request):
    return HttpResponse('loggedout.html')

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