from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from .models import Product, StaffSubmission
from .forms import HatOneForm, HatTwoForm, CloakForm, WandForm, StaffSubmissionForm


def calc_variables(variable_one, variable_two, variable_three, a, b, c, d, e, f):
    """
    Top level function to calculate the variables
    for each following custom product.
    """
    price = 20

    if variable_one == a:
        price = price + 5
    elif variable_one == b:
        price = price + 10
    elif variable_one == c:
        price = price + 15
    else:
        price + 0

    if variable_two == d:
        price = price + 5
    elif variable_two == e:
        price = price + 10
    elif variable_two == f:
        price = price + 15
    else:
        price = price + 0

    if variable_three == 'None':
        price = price + 0
    else:
        price = price + 2 

    return price


class DesignCustomHat(View):
    """
    Class to get a quote for a custom hat.
    """
    def get(self, request):
        form = HatOneForm()
        template = 'products/custom_hat_one.html'
        context = {
            'form': form,
        }

        return render(request, template, context)

    def post(self, request):
        form = HatOneForm(request.POST) 
        brim_width = request.POST['variable_one']
        hat_height = request.POST['variable_two']
        patch = request.POST['variable_three']
        
        if form.is_valid():
            priced_form = form.save(commit=False)
            priced_form.price = calc_variables(
                brim_width, hat_height, patch, 
                "Brim - 5cm", "Brim - 10cm", "Brim - 15cm", 
                "Height - 15cm", "Height - 20cm", "Height - 25cm")
            priced_form.product_type = "Hat"
            product = form.save()
            return redirect(reverse('final_quote', args=[product.id]))
        else:
            messages.error(request, 'Quote was not generated. Please try again.')
            form = HatOneForm()

        template = 'products/custom_hat_one.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


class DesignCustomHatTwo(View):
    """
    Class to get a quote for a second custom hat.
    """
    def get(self, request):
        form = HatTwoForm()

        template = 'products/custom_hat_two.html'
        context = {
            'form': form,
        }

        return render(request, template, context)

    def post(self, request):
        form = HatTwoForm(request.POST) 
        spell_choices = request.POST['variable_one']
        hat_floppiness = request.POST['variable_two']
        patch = request.POST['variable_three']

        if form.is_valid():
            priced_form = form.save(commit=False)
            priced_form.price = calc_variables(
                spell_choices, hat_floppiness, patch, 
                "Spell - Freeze", "Spell - Wither", "Spell - Overexplain", 
                "Fairly floppy", "Very floppy", "Very extremely floppy")
            priced_form.product_type = "Floppy Hat"
            product = form.save()
            return redirect(reverse('final_quote', args=[product.id]))
        else:
            messages.error(request, 'Quote was not generated. Please try again.')
            form = HatTwoForm()

        template = 'products/custom_hat_two.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


class DesignCustomCloak(View):
    """
    Class to get a quote for a custom cloak.
    """
    def get(self, request):
        form = CloakForm()

        template = 'products/custom_cloak.html'
        context = {
            'form': form,
        }

        return render(request, template, context)

    def post(self, request):
        form = CloakForm(request.POST) 
        cloak_length = request.POST['variable_one']
        cloak_pattern = request.POST['variable_two']
        clasp_choices = request.POST['variable_three']
        
        if form.is_valid():
            priced_form = form.save(commit=False)
            priced_form.price = calc_variables(
                cloak_length, cloak_pattern, clasp_choices, 
                "Length - Mini", "Length - Midi", "Length - So Long You Will Step On It", 
                "Pattern - Tartan", "Pattern - Leaves", "Pattern - Bowling alley carpet")
            priced_form.product_type = "Cloak"
            product = form.save()
            return redirect(reverse('final_quote', args=[product.id]))
        else:
            messages.error(request, 'Quote was not generated. Please try again.')
            form = CloakForm()

        template = 'products/custom_cloak.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


class DesignCustomWand(View):
    """
    Class to get a quote for a custom wand.
    """
    def get(self, request):
        form = WandForm()
        template = 'products/custom_wand.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


    def post(self, request):
        form = WandForm(request.POST) 
        wand_length = request.POST['variable_one']
        wand_point = request.POST['variable_two']
        starting_spells = request.POST['variable_three']
        
        if form.is_valid():
            priced_form = form.save(commit=False)
            priced_form.price = calc_variables(
                wand_length, wand_point, starting_spells, 
                "Length - 10cm", "Length - 15cm", "Length - 20cm", 
                "Point - Cactus", "Point - Orb", "Point - Ice Lolly")
            priced_form.product_type = "Wand"
            product = form.save()
            return redirect(reverse('final_quote', args=[product.id]))
        else:
            messages.error(request, 'Quote was not generated. Please try again.')
            form = WandForm()

        template = 'products/custom_wand.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


class StaffSubmitView(View):
    """
    Class for staff members to submit a request for a product.
    """
    def get(self, request):
        if not request.user.is_staff:
            messages.error(request, 'Apologies, only staff can access this.')
            return redirect(reverse('landing_page'))

        form = StaffSubmissionForm()

        template = 'products/staff_submission.html'
        context = {
            'form': form
        }

        return render(request, template, context)
    
    def post(self, request):
        form = StaffSubmissionForm(request.POST, request.FILES) 
        if form.is_valid():
            staff_form = form.save(commit=False)
            staff_form.staff_member = request.user
            form.save()
            return redirect(reverse('landing_page'))
        else:
            messages.error(request, 'Product was not submitted. Please try again.')
            form = StaffSubmissionForm()

        template = 'products/staff_submission.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


def all_products(request):
    """
    Function to retrieve all products.
    """
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)


def final_quote(request, product_id):
    """
    Function to display a quote for a custom product.
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/final_quote.html', context)
