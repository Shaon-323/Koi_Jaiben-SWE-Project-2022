from django.shortcuts import render
from decimal import Decimal

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Bus, Book, counter
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from  django.views.generic import ListView,CreateView
from  django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/home.html')
    else:
        return render(request, 'myapp/signin.html')


@login_required(login_url='signin')
def findbus(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('from')
        dest_r = request.POST.get('to')
        terminal_r = request.POST.get('terminal')
        date_r = request.POST.get('date')
        bus_list = Bus.objects.filter( terminal=terminal_r, source=source_r, dest=dest_r, date=date_r)
        if bus_list:
            return render(request, 'myapp/list.html', locals())
        else:
            context["error"] = "Sorry no buses availiable"
            return render(request, 'myapp/findbus.html', context)
    else:
        return render(request, 'myapp/findbus.html')


@login_required(login_url='signin')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        seats_r = int(request.POST.get('no_seats'))
        bus = Bus.objects.get(id=id_r)
        if bus:
            if bus.rem > int(seats_r):
                name_r = bus.bus_name
                cost = int(seats_r) * bus.price
                source_r = bus.source
                dest_r = bus.dest
                nos_r = Decimal(bus.nos)
                price_r = bus.price
                date_r = bus.date
                time_r = bus.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = bus.rem - seats_r
                Bus.objects.filter(id=id_r).update(rem=rem_r)
                book = Book.objects.create(name=username_r, email=email_r, userid=userid_r, bus_name=name_r, source=source_r, busid=id_r,dest=dest_r, price=price_r, nos=seats_r, date=date_r, time=time_r)
                return render(request, 'myapp/payment.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'myapp/findbus.html', context)

    else:
        return render(request, 'myapp/findbus.html')


@login_required(login_url='signin')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        try:
            book = Book.objects.get(id=id_r)
            bus = Bus.objects.get(id=book.busid)
            rem_r = bus.rem + book.nos
            Bus.objects.filter(id=book.busid).update(rem=rem_r)
            Book.objects.filter(id=id_r).delete()
            return redirect(seebookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that bus"
            return render(request, 'myapp/error.html', context)
    else:
        return render(request, 'myapp/findbus.html')


@login_required(login_url='signin')
def seebookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'myapp/booklist.html', locals())
    else:
        context["error"] = "Sorry no buses booked"
        return render(request, 'myapp/findbus.html', context)


def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            login(request, user)
            return render(request, 'myapp/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signup.html', context)
    else:
        return render(request, 'myapp/signup.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            # username = request.session['username']
            context["user"] = name_r
            context["id"] = request.user.id
            return render(request, 'myapp/home.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'myapp/signin.html', context)

#@login_required(login_url='signin')
class counter(LoginRequiredMixin, CreateView):
    model = counter
    fields = ['Name', 'Terminal']
    template_name = 'myapp/add_counter.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.User = self.request.user
        return super().form_valid(form)

#@login_required(login_url='signin')
class bus(LoginRequiredMixin, CreateView):
    model = Bus
    fields = ['terminal', 'bus_name', 'coach_number', 'source', 'dest', 'nos', 'rem', 'price', 'date', 'time', 'arrival_time']
    template_name = 'myapp/bus.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.User = self.request.user
        return super().form_valid(form)

@login_required(login_url='signin')
def payment(request):
    if request.method == 'POST':
        bus_id = request.POST.get('bus_id')
        num = request.POST.get('num')
        amount = request.POST.get('amount')
        Book.objects.filter(id=bus_id).update(status='Done')
        book = Book.objects.get(id=bus_id)
        return render(request, 'myapp/bookings.html', locals())

def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'myapp/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'myapp/success.html', context)


'''@login_required(login_url='signin')
def profile(request):
    context = {}
    profile = User.objects.get(username = request.user)
    if profile:
        return render(request, 'myapp/profile.html', locals())
    else:
        context['error'] = 'No profile information available. To set your profile information click Edit button'
        return render(request, 'myapp/profile.html', context)'''

#def edit_profile(request):
