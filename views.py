from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView, UpdateView
from accounts.models import User
from accounts.forms import UserPhoneForm, ConfirmForm
from phonehome.models import Recording


class IndexView(TemplateView):
    template_name = 'index.html'

from phonehome.sendsms import send, fetch_code


from django.contrib.auth.decorators import login_required


@login_required()
def GiveNumberView(request):

    template_name = 'givenumber.html'

    if request.method == 'POST':
        form = UserPhoneForm(request.POST)
        if form.is_valid():



            form.save()

            code = fetch_code()

            request.user.code = code.upper()
            request.user.save()
            send(request.user.first_name, code,form['phone'].value())

            return HttpResponseRedirect('/confirmnumber/')
    else:
        form = UserPhoneForm()

    return render(request, template_name, {
        'form': form,
        })

@login_required()
def ConfirmNumberView(request):

    template_name = 'confirmnumber.html'

    if request.method == 'POST':
        form = ConfirmForm(request.POST)
        if form.is_valid():



            if request.user.code == form['code'].value():

                return HttpResponseRedirect('/tryit/')
            else:
                form = ConfirmForm()

    else:
        form = ConfirmForm()

    return render(request, template_name, {
        'form': form,
        })



"""
class ConfirmNumberView(TemplateView):
    template_name = 'confirmnumber.html'


class ScheduleView(TemplateView):
    template_name = 'schedule.html'


class SaveInContactsView(TemplateView):
    template_name = 'saveincontacts.html'
"""

@login_required()
def TryItView(request):
    return render(request, 'tryit.html', { 'phone': request.user.phone, })

@login_required()
def PlayerView(request, id=0):
    try:
        recording = Recording.objects.get(id=id)
    except:
        return HttpResponseRedirect(reverse('index'))

    caller = User.objects.get(phone=recording.recipient.replace("+1",""))

    return direct_to_template(request, template='player.html',
        extra_context={'url':recording.url, 'caller':caller, 'id': recording.id, 'name': recording.fb_user_name})

@login_required()
def birthdays(request):
    data = request.user.create_call()
    return HttpResponse(data)
