from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def farmer_view(request):
    return render(request, 'farmer.html')

def tourists_view(request):
    return render(request, 'tourists.html')
def register_farmer(request):
    return render(request, 'signup.html')

def courses_view(request):
    return render(request, 'courses.html')

def products_view(request):
    return render(request, 'products.html')
# views.py

from django.shortcuts import render
from .models import Farm

def lend_a_farm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        farm_name = request.POST.get('farm-name')
        location = request.POST.get('location')
        type_of_soil = request.POST.get('type-of-soil')
        type_of_crop = request.POST.get('type-of-crop')
        description = request.POST.get('description')
        
        # Create and save a new Farm instance
        farm = Farm.objects.create(
            name=name,
            email=email,
            phone=phone,
            farm_name=farm_name,
            location=location,
            type_of_soil=type_of_soil,
            type_of_crop=type_of_crop,
            description=description
        )
        farm.save()
        return render(request, 'farmer.html')  # Redirect to a success page after submission
    else:
        return render(request, 'lendafarm.html')  # Render the form page for GET requests

def centres(request):
    # Fetch all farm objects from the database
    farms = Farm.objects.all()
    # Pass the farms variable to the template
    return render(request, 'centres.html', {'farms': farms})

def agritourism_centres(request):
    # Fetch all farm details from the database
    farms = Farm.objects.all()
    context = {
        'farms': farms
    }
    return render(request, 'agritourism_centres.html', context)

# views.py

from django.shortcuts import render, redirect
from .models import Farmer

def register_farmer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if password == confirm_password:
            farmer = Farmer(username=username, password=password)
            farmer.save()
            return redirect('login')  # Redirect to home page after successful signup
    else:
            # Handle password mismatch error
        if request.user.is_authenticated:
            return redirect('farmer')  # Redirect to the farmer's page
        else:
            return render(request, 'signup.html')

from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Farmer  # Import the Farmer model

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user against the default User model
        user = authenticate(username=username, password=password)

        if user is not None:
            # User authentication successful, log in the user
            auth_login(request, user)
            return redirect('farmer')  # Redirect to farmer page after successful login
        else:
            # Check if the username and password match in the Farmer model
            try:
                farmer = Farmer.objects.get(username=username, password=password)
                # If a match is found, create a session or perform required login actions
                request.session['farmer_id'] = farmer.id
                request.session['farmer_username'] = farmer.username
                return redirect('farmer')  # Redirect to farmer page after successful login
            except Farmer.DoesNotExist:
                # If no match found in Farmer model, show error message
                messages.error(request, 'Invalid username or password')
                return redirect('login')  # Redirect to login page with error message
    else:
        return render(request, 'login.html')

from .models import Blog
def blog_view(request):
    # Fetch all blog objects from the database
    blogs = Blog.objects.all()
    # Pass the blogs variable to the template
    return render(request, 'blog.html', {'blogs': blogs})



def write_blog_view(request):
    if request.method == 'POST':
        title = request.POST.get('blog-title')
        content = request.POST.get('blog-content')
        # Create a new Blog instance and save it to the database
        blog = Blog.objects.create(title=title, content=content)
        return redirect('blog')  # Redirect to the blog page after successful submission
    return render(request, 'writeblog.html')
