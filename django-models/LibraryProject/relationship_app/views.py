from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.shortcuts import render
from django.views.generic.detail import DetailView   # REQUIRED EXACT LINE
from .models import Book
from .models import Library

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile


def list_books(request):
    books = Book.objects.all()
    return render(
        request,
        "relationship_app/list_books.html",
        {"books": books}
    )

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

'''
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")  # Redirect anywhere you want
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Logout view
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

# Registration view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")  # Redirect after registration
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
'''

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, "relationship_app/register.html", {"form": form})


@user_passes_test(lambda user: hasattr(user, "userprofile") and user.userprofile.role == "Admin")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(lambda user: hasattr(user, "userprofile") and user.userprofile.role == "Librarian")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(lambda user: hasattr(user, "userprofile") and user.userprofile.role == "Member")
def member_view(request):
    return render(request, "relationship_app/member_view.html")



