from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView, UpdateView
from accounts.models import User
from accounts.forms import UserPhoneForm, ConfirmForm
from phonehome.models import Recording
from phonehome.sendsms import send, fetch_code
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = 'index.html'


@login_required()
def GiveNumberView(request):
    if request.method == 'POST':
        form = UserPhoneForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            code = fetch_code()

            request.user.code = code.upper()
            request.user.save()
            send(request.user.first_name, code,form['phone'].value())

            return HttpResponseRedirect(reverse('confirmnumber'))
    else:
        form = UserPhoneForm()

    return render(request, 'givenumber.html', {
        'form': form,
        })

@login_required()
def ConfirmNumberView(request):
    if request.method == 'POST':
        form = ConfirmForm(request.POST, instance=request.user)
        if form.is_valid():
            return HttpResponseRedirect(reverse('tryit'))
    else:
        form = ConfirmForm()

    return render(request, 'confirmnumber.html', {
        'form': form,
        })



"""
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
