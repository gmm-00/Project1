from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives

from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required


def recipes(request):
    email=''
    if request.method == 'POST':
        email = request.POST.get('email')
        recipe_name = request.POST.get('recipe_name')
        recipe_des = request.POST.get('recipe_des')
        recipe_image = request.FILES.get('recipe_image')

        # if email and recipe_name and recipe_des:
        #     Recipe.objects.create(email=email, recipe_name=recipe_name, recipe_des=recipe_des, recipe_image=recipe_image)

        #     subject, from_email, to = "Recipes Email", "p1ashok36@gmail.com", email
        #     text_content = "This is an important message."
        #     html_content = "<b>This is a sample welcome message for Adding Recipes.</b>"
            
        #     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        #     msg.attach_alternative(html_content, "text/html")
        #     msg.send()


            # return redirect('recipes')  # Redirect to the same URL after successful form submission

    recipes = Recipe.objects.all()

    if request.GET.get('search'):
    	recipes=recipes.filter(recipe_name__icontains=request.GET.get('search'))

    context={'details':recipes}
    return render(request, 'recipe.html',context)

@login_required(login_url="/login/")    
def delete_recipes(request,id):

 	dele=Recipe.objects.get(id=id)
 	dele.delete()

 	return redirect('recipes')

@login_required(login_url="/login/")
def update_recipes(request, id):
    update_recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':

        email = request.POST.get('email')
        recipe_name = request.POST.get('recipe_name')
        recipe_des = request.POST.get('recipe_des')
        recipe_image = request.FILES.get('recipe_image')

        update_recipe.email = email
        update_recipe.recipe_name = recipe_name
        update_recipe.recipe_des = recipe_des

        if recipe_image:
            update_recipe.recipe_image = recipe_image

        update_recipe.save()



        return redirect('recipes')  # Redirect to the home page after successful update

    context = {'update': update_recipe}
    return render(request, 'update.html', context)



def login_page(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username = username).exists():

            messages.error(request, "Invalid username!")

            return redirect('/login/')
                
        user = authenticate(username =username , password = password)

        if user is None:
            messages.error(request, "Invalid PASSWORD!")
            return redirect('/login/')

        else:
            login(request , user)
            return redirect('recipes')


    return render(request , 'login.html')


def register(request):

    if request.method == 'POST':

        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.error(request, "Username already exists!!")

            return redirect('/register')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            

            )


        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully")

        return redirect('/login/')


    return render(request , 'register.html')


def logout_page(request):

    logout(request)
    messages.success(request, "Successfully Logout")
    return redirect('/login/')