from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm, CustomerAuthenticationForm

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
                login(request, customer)
                return redirect('success')  # Redirect to success page after successful login
    else:
        form = CustomerAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def success(request):
    # Ensure only logged-in users can access this view
    return render(request, 'accounts/success.html')




