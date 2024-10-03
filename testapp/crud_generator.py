from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import path

def generate_crud_urls(defModels, app_name):
    """
    Automatically generate CRUD views and URLs for a given model. 
    """
    class ModelCreateView(CreateView):
        model = defModels
        fields = '__all__'
        success_url = '/'
        template_name = f'{app_name}/{defModels.__name__.lower()}_form.html'
    
    class ModelUpdateView(UpdateView):
        model = defModels
        fields = '__all__'
        success_url = '/'
        template_name = f'{app_name}/{defModels.__name__.lower()}_form.html'
    
    class ModelDeleteView(DeleteView):
        model = defModels
        success_url = '/'
        template_name = f'{app_name}/{defModels.__name__.lower()}_confirm_delete.html'
    
    class ModelListView(ListView):
        model = defModels
        template_name = f'{app_name}/{defModels.__name__.lower()}_list.html'

        def get_context_data(self, **kwargs):
            # Get the context from the parent class
            context = super().get_context_data(**kwargs)
            # Add the model name to the context
            context['model_name'] = self.model.__name__
            return context
    
    class ModelDetailView(DetailView):
        model = defModels
        template_name = f'{app_name}/{defModels.__name__.lower()}_detail.html'

        def get_context_data(self, **kwargs):
            # Get the context from the parent class
            context = super().get_context_data(**kwargs)
            # Add the model name to the context
            context['model_name'] = self.model.__name__
            return context

    model_name = defModels.__name__.lower()
    return [
        path(f'{model_name}/create/', ModelCreateView.as_view(), name=f'{model_name}_create'),
        path(f'{model_name}/<int:pk>/edit/', ModelUpdateView.as_view(), name=f'{model_name}_edit'),
        path(f'{model_name}/<int:pk>/delete/', ModelDeleteView.as_view(), name=f'{model_name}_delete'),
        path(f'{model_name}/', ModelListView.as_view(), name=f'{model_name}_list'),
        path(f'{model_name}/<int:pk>/', ModelDetailView.as_view(), name=f'{model_name}_detail'),
    ]
 