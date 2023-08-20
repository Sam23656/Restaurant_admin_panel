from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from Panel.forms import AddFoodForm
from Panel.models import Food


# Create your views here.

class FoodListView(ListView):
    model = Food
    template_name = "index.html"
    context_object_name = "foods"


class AddFoodView(CreateView):
    model = Food
    form_class = AddFoodForm
    template_name = "add_food.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('food_detail', kwargs={'slug_param': self.object.slug})


class FoodDetailView(DetailView):
    model = Food
    template_name = "food_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug_param"


class FoodDeleteView(DeleteView):
    model = Food
    template_name = "delete_food.html"
    slug_url_kwarg = "slug_param"
    success_url = reverse_lazy("index")


class FoodUpdateView(UpdateView):
    model = Food
    form_class = AddFoodForm
    template_name = "update_food.html"
    slug_url_kwarg = "slug_param"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('food_detail', kwargs={'slug_param': self.object.slug})
