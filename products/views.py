from django.shortcuts import render, redirect
from products.forms import ProductCreateForms, CommentCreateForms
from products.models import Product, Comment


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_page_view(request):
    if request.method == 'GET':

        products = Product.objects.all()

        context = {
            'products': products
        }

        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':

        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': CommentCreateForms
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        form = CommentCreateForms(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                products_id=id
            )

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': form
        }

        return render(request, 'products/detail.html', context=context)


def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForms
        }
        return render(request, 'products/create.html', context)

    if request.method == 'POST':
        form = ProductCreateForms(request.POST, request.FILES)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                rate=form.cleaned_data.get('rate'),
            )
            return redirect('/products/')

        context = {
            'form': form
        }

        return render(request, 'products/create.html', context=context)
