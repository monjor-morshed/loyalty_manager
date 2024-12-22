from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm, CustomerAuthenticationForm
from django.contrib.auth import logout


def index(request):
    return render(request, 'accounts/index.html')

def register(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            login(request, customer)
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = CustomerForm()
    return render(request, 'accounts/register.html', {'form': form})

def c_login(request):
    if request.method == 'POST':
        form = CustomerAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            customer = authenticate(request, username=username, password=password)
            if customer is not None:
                login(request, customer) #
                return redirect('make_purchase')  # Redirect to success page after successful login
    else:
        form = CustomerAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def success(request):
    return render(request, 'accounts/success.html')

@login_required
def make_purchase(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        request.user.add_points(amount)

        return redirect('view_points')
    return render(request, 'accounts/make_purchase.html')

@login_required
def redeem_points(request):
    if request.method == 'POST':
        points_to_redeem = int(request.POST.get('points'))
        try:
            # request.user.discount += request.user.redeem_points(points_to_redeem)
            discount = request.user.redeem_points(points_to_redeem)
            request.session['discount'] = discount
        except ValueError as e:
            messages.error(request, str(e))
        return redirect('view_discount')
    return render(request, 'accounts/redeem_points.html')


@login_required
def view_points(request):
    user_points = request.user.individual_points
    return render(request, 'accounts/view_points.html', {'points': user_points})

@login_required
def view_discount(request):
    user_points = request.user.individual_points
    user_discount = request.session.get('discount', 0)
    return render(request, 'accounts/view_discount.html', {'points': user_points, 'discount': user_discount}, )

def c_logout(request):
    logout(request)
    return redirect('login')



