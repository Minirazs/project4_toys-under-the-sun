from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .forms import ToyForm, SearchForm
from .models import Toy
from django.db.models import Q

# Create your views here.


def redirect_view(request):
    response = redirect('/toy/')
    return response


def index(request):
    toys = Toy.objects.all()
    search_form = SearchForm()

    return render(request, 'toy/index.template.html', {
        'toys': toys,
        'search_form': search_form
    })


def search(request):
    # a query set that represents ALL the toys
    toy_query = Toy.objects.all()

    search_form = SearchForm()

    # create an empty query  -- represents ALWAYS TRUE
    queries = ~Q(pk__in=[])

    # check if the user has submitted anything
    if request.GET:
        # if the user has filled in the title
        print(request.GET)
        if 'title' in request.GET and request.GET['title'] and request.GET['title'] != "":
            queries = queries & Q(title__icontains=request.GET['title'])

        if 'age' in request.GET and request.GET['age']:
            queries = queries & Q(age__in=request.GET.getlist('age'))

        if 'country' in request.GET and request.GET['country']:
            queries = queries & Q(country__in=request.GET.getlist('country'))

        if 'category' in request.GET and request.GET['category']:
            queries = queries & Q(category__in=request.GET.getlist('category'))

    # sandbox
    # queries = queries & Q(title__icontains="rings")
    # queries = queries & Q(tags__in=[2])
    # endsandbox

    all_toys = toy_query.filter(queries)

    for i in all_toys:
        i.price = float(i.price/100)

    return render(request, 'toy/search.template.html', {
        'toys': all_toys,
        'search_form': search_form
    })


# show details of a specific toy


def one_toy(request, toy_id):
    toy = get_object_or_404(Toy, pk=toy_id)
    print(toy.cover.url)

    toy.price = float(toy.price/100)

    return render(request, 'toy/one_toy.template.html', {
        'toy': toy
    })


@staff_member_required
def create_toy(request):
    if request.method == 'POST':  # 1

        create_form = ToyForm(request.POST)  # 2

        # check if the form has valid values
        if create_form.is_valid():  # 3
            create_form.save()  # 4
            messages.success(
                request, f"New toy {create_form.cleaned_data['title']} has been created")
            return redirect(reverse(index))
        else:
            # 5. if does not have valid values, re-render the form
            return render(request, 'toy/create.template.html', {
                'form': create_form
            })
    else:
        create_form = ToyForm()
        return render(request, 'toy/create.template.html', {
            'form': create_form
        })


@staff_member_required
def update_toy(request, toy_id):
    # 1. retrieve the toy which we are editing
    toy_being_updated = get_object_or_404(Toy, pk=toy_id)

    # 2 - create the form and fill it with data from toy instance
    if request.method == "POST":
        toy_form = ToyForm(request.POST, instance=toy_being_updated)

        # 3. create the form and fill in the user's data. Also specify that
        # this is to update an existing model (the instance argument)
        if toy_form.is_valid():
            toy_form.save()
            return redirect(reverse(index))

        else:
            return render(request, 'toy/update.template.html', {
                "form": toy_form
            })
    else:
        # 4. create a form with the toy details filled in
        toy_form = ToyForm(instance=toy_being_updated)

        return render(request, 'toy/update.template.html', {
            "form": toy_form
        })


@staff_member_required
def delete_toy(request, toy_id):

    if request.method == 'POST':
        toy_to_delete = get_object_or_404(Toy, pk=toy_id)
        toy_to_delete.delete()
        return redirect(index)
    else:
        toy_to_delete = get_object_or_404(Toy, pk=toy_id)
        return render(request, 'toy/delete.template.html', {
            "toy": toy_to_delete
        })
