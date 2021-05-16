from django.shortcuts import render, redirect
from .models import Staff, Blog
from .form import ContactUsForm
from django.contrib import messages
# Create your views here.

def index(request):
    # employ = Employees.objects.all()
    # return render(request, 'index.html', {'employee': employ})
    blog = Blog.objects.all()
    return render(request, 'myweb/index.html', {'blog': blog})
def about(request):
    staff = Staff.objects.all()
    return render(request, 'myweb/about.html', {'pst': staff})
def blog(request):
    blog = Blog.objects.all()
    return render(request, 'myweb/blog-grid.html', {'blog': blog})
def singleblog(request, slug):
    item = Blog.objects.get(slug=slug)
    return render(request, 'myweb/blog-single.html', {"item": item})
def contact_us(request):
    if request.method == 'POST':
        f = ContactUsForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted')
            return redirect('index')
        else:
            f = ContactUsForm()
        return render(request, 'myweb/contact.html', {'form': f, 'messages':messages})
def regis(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = ContactUsForm()
    return render(request, 'myweb/contact.html', {'form': form})