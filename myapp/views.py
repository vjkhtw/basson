from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, FoodCategory, FoodWaste, WasteCategory
from .forms import FoodForm, FoodWasteForm, FoodCategoryForm, WasteCategoryForm


def home(request):
    return render(request, 'myapp/home.html')

def food_list(request):
    categories = FoodCategory.objects.prefetch_related('food_set').all()
    context = {'categories': categories}
    return render(request, 'myapp/food_list.html', context)

def food_create(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm()
    return render(request, 'myapp/food_create.html', {'form': form})

def food_update(request, pk):
    food = Food.objects.get(pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm(instance=food)
    return render(request, 'myapp/food_update.html', {'form': form, 'food': food})

def food_detail(request, pk):
    food = Food.objects.get(pk=pk)
    return render(request, 'myapp/food_detail.html', {'food': food})

def food_delete(request, pk):
    food = Food.objects.get(pk=pk)
    food.delete()
    return redirect('food_list')

def foodwaste_list(request):
    categories = WasteCategory.objects.prefetch_related('foodwaste_set').all()
    context = {'categories': categories}
    return render(request, 'myapp/foodwaste_list.html', {'categories': categories})

def foodwaste_create(request):
    if request.method == 'POST':
        form = FoodWasteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foodwaste_list')
    else:
        form = FoodWasteForm()
    return render(request, 'myapp/foodwaste_create.html', {'form': form})

def foodwaste_update(request, pk):
    foodwaste = FoodWaste.objects.get(pk=pk)
    if request.method == 'POST':
        form = FoodWasteForm(request.POST, instance=foodwaste)
        if form.is_valid():
            form.save()
            return redirect('foodwaste_list')
    else:
        form = FoodWasteForm(instance=foodwaste)
    return render(request, 'myapp/foodwaste_update.html', {'form': form, 'foodwaste': foodwaste})

def foodwaste_detail(request, pk):
    foodwaste = FoodWaste.objects.get(pk=pk)
    return render(request, 'myapp/foodwaste_detail.html', {'foodwaste': foodwaste})

def foodwaste_delete(request, pk):
    food = FoodWaste.objects.get(pk=pk)
    food.delete()
    return redirect('foodwaste_list')

def foodcategory_list(request):
    categories = FoodCategory.objects.all()
    return render(request, 'myapp/foodcategory_list.html', {'food_categories': categories})

def foodcategory_create(request):
    if request.method == 'POST':
        form = FoodCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foodcategory_list')
    else:
        form = FoodCategoryForm()
    return render(request, 'myapp/foodcategory_create.html', {'form': form})

def foodcategory_update(request, pk):
    category = FoodCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = FoodCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('foodcategory_list')
    else:
        form = FoodCategoryForm(instance=category)
    return render(request, 'myapp/foodcategory_update.html', {'form': form, 'category': category})

def foodcategory_detail(request, pk):
    category = FoodCategory.objects.get(pk=pk)
    return render(request, 'myapp/foodcategory_detail.html', {'category':category})

def foodcategory_delete(request, pk):
    category = FoodCategory.objects.get(pk=pk)
    category.delete()
    return redirect('foodcategory_list')

def wastecategory_list(request):
    categories = WasteCategory.objects.all()
    return render(request, 'myapp/wastecategory_list.html', {'waste_categories': categories})

def wastecategory_create(request):
    if request.method == 'POST':
        form = WasteCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wastecategory_list')
    else:
        form = WasteCategoryForm()
    return render(request, 'myapp/wastecategory_create.html', {'form': form})

def wastecategory_update(request, pk):
    category = WasteCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = WasteCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('wastecategory_list')
    else:
        form = WasteCategoryForm(instance=category)
    return render(request, 'myapp/wastecategory_update.html', {'form': form, 'category': category})

def wastecategory_detail(request, pk):
    category = WasteCategory.objects.get(pk=pk)
    return render(request, 'myapp/wastecategory_detail.html', {'category':category})

def wastecategory_delete(request, pk):
    category = WasteCategory.objects.get(pk=pk)
    category.delete()
    return redirect('wastecategory_list')

