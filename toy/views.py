from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import ToyForm
from .models import Toy

# Create your views here.


def index(request):
    toys = Toy.objects.all()

    return render(request, 'toy/index.template.html', {
        'toys': toys
    })


@login_required
def create_toy(request):
    if request.method == 'POST':  # 1

        create_form = ToyForm(request.POST)  # 2

        # check if the form has valid values
        if create_form.is_valid():  # 3
            create_form.save()  # 4
            messages.success(request, f"New toy {create_form.cleaned_data['title']} has been created")
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


@login_required
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


@login_required
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