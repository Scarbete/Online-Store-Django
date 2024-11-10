from django.shortcuts import render, redirect
from products.forms import ProductCreateForms, CommentCreateForms
from products.models import Product, Comment
from products.contsants import PAGINATION_LIMIT
from django.views.generic import ListView, DetailView, CreateView


class MainPageCBV(ListView):
    model = Product
    template_name = 'layouts/index.html'


class ProductsCBV(ListView):
    model = Product
    template_name = 'products/products.html'

    def get(self, request, **kwargs):
        products = self.model.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search:
            products = products.filter(title__icontains=search) | products.filter(description__icontains=search)

        max_page = products.__len__() / PAGINATION_LIMIT

        max_page = round(max_page) + 1 if round(max_page) < max_page else round(max_page)

        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page + 1),
        }

        return render(request, self.template_name, context=context)


class ProductDetailCBV(DetailView, CreateView):
    model = Product
    template_name = 'products/detail.html'
    form_class = CommentCreateForms

    def get(self, request, **kwargs):
        id = int(kwargs['id'])
        product = self.model.objects.get(id=id)

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': self.form_class,
            'user': request.user,
        }

        return render(request, self.template_name, context=context)

    def post(self, request, **kwargs):
        id = int(kwargs['id'])
        product = Product.objects.get(id=id)
        form = self.form_class(data=request.POST)

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

        return render(request, self.template_name, context=context)


class CreateProductCBV(ListView, CreateView):
    model = Product
    template_name = 'products/create.html'
    form_class = ProductCreateForms

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': kwargs['form'] if kwargs.get('form') else self.form_class
        }

    def get(self, request, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, **kwargs):
        form = ProductCreateForms(request.POST, request.FILES)

        if form.is_valid():
            self.model.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                rate=form.cleaned_data.get('rate'),
            )
            return redirect('/products/')

        return render(request, self.template_name, context=self.get_context_data(form=form))
