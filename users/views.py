from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterForm, LoginForm
from django.views.generic import ListView, CreateView
from django.views import View


class RegisterCBV(ListView, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = RegisterForm

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': kwargs['form'] if kwargs.get('form') else self.form_class
        }

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())

    def post(self, request, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                self.model.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1'),
                )
                return redirect('/users/login/')
            else:
                form.add_error('password1', 'Пароли не совпадают!')

            return render(request, self.template_name, context=self.get_context_data(form=form))


class LoginCBV(ListView, CreateView):
    model = User
    template_name = 'users/login.html'
    form_class = LoginForm

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': kwargs['form'] if kwargs.get('form') else self.form_class
        }

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())

    def post(self, request, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )

            if user:
                login(request, user)
                return redirect('/products/')
            else:
                form.add_error('username', 'Authenticate error, try again')

        return render(request, self.template_name, context=self.get_context_data(form=form))


class LogoutCBV(View):
    def get(self, request, **kwargs):
        logout(request)
        return redirect('/products/')
