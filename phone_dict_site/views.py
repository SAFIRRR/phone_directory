from django.shortcuts import render
from .models import Employee, Building
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

@login_required(login_url='/admin/login/?next=/')
def full_phone_dict(request):
    if request.GET.get('search_field'):
        search = request.GET.get('search_field')
        if '@' in search and '.' in search:
            data = Employee.objects.filter(mail__icontains = search)

        elif '+' in search and '(' in search and ')' in search and '-' in search:
            data = Employee.objects.filter(ext_phone = search)

        elif '@' not in search and '.' not in search:
            data = Employee.objects.filter(
                Q(displayName__iregex = search) | Q(subdivision__name__iregex = search))


    elif request.method == 'GET':
        data = Employee.objects.order_by('subdivision')

    context = {'data': data}
    return render(request, 'index.html', context=context)

def visible_phone_dict(request):
    if request.GET.get('search_field'):
        search = request.GET.get('search_field')
        if '@' in search and '.' in search:
            data = Employee.objects.filter(visible = True, mail__icontains = search)

        elif '+' in search and '(' in search and ')' in search and '-' in search:
            data = Employee.objects.filter(visible = True, ext_phone = search)

        elif '@' not in search and '.' not in search:
            data = Employee.objects.filter(visible = True, displayName__iregex = search)

    elif request.method == 'GET':
        data = Employee.objects.filter(visible=True).order_by('subdivision')

    context = {'data': data}
    return render(request, 'visible_phone_dict.html', context=context)