from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from .models import Post
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm


# Home (latest 5 posts)
def home(request):
    posts = Post.objects.order_by('-published_date')[:5]
    return render(request, "blog/home.html", {"posts": posts})


# Registration
def register(request):
    if request.user.is_authenticated:
        return redirect("blog:profile")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account was created. You can now log in.")
            return redirect("blog:login")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


# Profile Update
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("blog:profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, "blog/profile.html", {"u_form": u_form, "p_form": p_form})


# --- Blog Post Views ---

# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('-published_date')


# Show single post details
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    from django.urls import reverse_lazy
    success_url = reverse_lazy('blog:post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
