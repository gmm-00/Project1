from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Removed EmailMultiAlternatives as it's no longer used

@login_required(login_url="/login/")
def recipes(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        recipe_name = request.POST.get('recipe_name')
        recipe_des = request.POST.get('recipe_des')
        recipe_image = request.FILES.get('recipe_image')

        if email and recipe_name and recipe_des:
            Recipe.objects.create(
                email=email,
                recipe_name=recipe_name,
                recipe_des=recipe_des,
                recipe_image=recipe_image
            )
            messages.success(request, "Recipe added successfully.")
            return redirect('recipes')
        else:
            messages.error(request, "Please fill in all the fields.")

    recipes = Recipe.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        recipes = recipes.filter(recipe_name__icontains=search_query)

    context = {'details': recipes}
    return render(request, 'recipe.html', context)

@login_required(login_url="/login/")
def delete_recipes(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    messages.success(request, "Recipe deleted successfully.")
    return redirect('recipes')

@login_required(login_url="/login/")
def update_recipes(request, id):
    update_recipe = get_object_or_404(Recipe, id=id)

    if request.method == 'POST':
        email = request.POST.get('email')
        recipe_name = request.POST.get('recipe_name')
        recipe_des = request.POST.get('recipe_des')
        recipe_image = request.FILES.get('recipe_image')

        if email and recipe_name and recipe_des:
            update_recipe.email = email
            update_recipe.recipe_name = recipe_name
            update_recipe.recipe_des = recipe_des

            if recipe_image:
                update_recipe.recipe_image = recipe_image

            update_recipe.save()
            messages.success(request, "Recipe updated successfully.")
            return redirect('recipes')
        else:
            messages.error(request, "Please fill in all the fields.")

    context = {'update': update_recipe}
    return render(request, 'update.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username!")
            return redirect('/login/')
                
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid password!")
            return redirect('/login/')
        else:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('recipes')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        username   = request.POST.get('username')
        password   = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('/register')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('/login/')

    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('/login/')
