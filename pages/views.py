from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Page

# View para listar todas as páginas do blog
class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'

# View para exibir detalhes de uma página específica
class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'

# View para criar uma nova página, restrita a administradores
class PageCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:page_list')

    def test_func(self):
        return self.request.user.is_staff  # Apenas administradores

    def form_valid(self, form):
        form.instance.author = self.request.user  # Define o autor como o usuário logado
        return super().form_valid(form)

# View para atualizar uma página existente, restrita a administradores
class PageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:page_list')

    def test_func(self):
        return self.request.user.is_staff  # Apenas administradores

# View para excluir uma página, restrita a administradores
class PageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:page_list')

    def test_func(self):
        return self.request.user.is_staff  # Apenas administradores