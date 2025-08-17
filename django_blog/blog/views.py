from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from django.urls import reverse_lazy

from .models import Post, Profile
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm


# Home (latest 5 published posts)
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
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


# Profile Update (safe even if Profile doesn't yet exist)
@login_required
def profile(request):
    # Ensure profile exists for this user
    profile_obj, _created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile_obj)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("blog:profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile_obj)

    return render(request, "blog/profile.html", {"u_form": u_form, "p_form": p_form})


# --- Blog Post Views ---

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        # Only show published posts publicly
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        # Option A: publish immediately (uncomment next line)
        form.instance.published_date = timezone.now()
        # Option B: leave as draft (comment out the line above)
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # Keep author intact as current user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Optional: manual publish endpoint (useful if you allow drafts)
@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.publish()
        messages.success(request, "Post published successfully.")
    return redirect('blog:post-detail', pk=pk)


print("publish_post in globals:", "publish_post" in globals())


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from django.utils import timezone

@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.publish()
        messages.success(request, "Post published successfully.")
    return redirect('blog:post-detail', pk=pk)
