from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Article
from .forms import ArticleForm  # Make sure you have this form created

# View to list all articles (requires can_view permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'bookshelf/article_list.html', {'articles': articles})


# View to create a new article (requires can_create permission)
@permission_required('bookshelf.can_create', raise_exception=True)
@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_by = request.user
            article.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'bookshelf/article_form.html', {'form': form})


# View to update an article (requires can_edit permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user != article.created_by and not request.user.is_superuser:
        return redirect('article_list')  # Or raise 403
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'bookshelf/article_form.html', {'form': form})


# View to delete an article (requires can_delete permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user != article.created_by and not request.user.is_superuser:
        return redirect('article_list')  # Or raise 403
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'bookshelf/article_confirm_delete.html', {'article': article})
