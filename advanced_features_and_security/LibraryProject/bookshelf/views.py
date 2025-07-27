from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import ExampleForm
from .models import Book
from .forms import BookForm

class BookListView(PermissionRequiredMixin, ListView):
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'
    permission_required = 'bookshelf.can_view'
    raise_exception = True

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookshelf/book_form.html'
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_create'
    raise_exception = True

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'bookshelf/book_form.html'
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_edit'
    raise_exception = True

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'bookshelf/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_delete'
    raise_exception = True

# ✅ Secure Search View (Safe from SQL Injection)
def search_books(request):
    query = request.GET.get("q", "").strip()
    books = Book.objects.filter(title__icontains=query) if query else []
    return render(request, "bookshelf/book_search_results.html", {"books": books, "query": query})

def get_queryset(self):
    return Book.objects.filter(created_by=self.request.user)
