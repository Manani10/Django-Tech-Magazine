from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Article, Category, Comment
from .forms import CommentForm

"""
This module contains views for the tech magazine application, 
including home, category detail, and article detail views.
"""

def home(request):
    """
    Displays the homepage with a list of articles and categories.
    """
    articles = Article.objects.all()
    categories = Category.objects.all()
    return render(request, 'magazine/home.html', {'articles': articles, 'categories': categories})

def category_detail(request, category_id):
    """
    Displays a list of articles under a specific category.
    """
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category)
    return render(request, 'magazine/category_detail.html', {'category': category, 'articles': articles})

def article_detail(request, article_id):
    """
    Displays an article with the option to add a comment.
    """
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = CommentForm()

    return render(request, 'magazine/article_detail.html', {'article': article, 'form': form})

def register(request):
    """
    Handles user registration using Django's built-in UserCreationForm.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'magazine/register.html', {'form': form})

@login_required
def profile(request):
    """
    Displays the profile page of the currently logged-in user.
    """
    user_articles = Article.objects.filter(author=request.user)
    return render(request, 'magazine/profile.html', {'user_articles': user_articles})

@login_required
def add_comment(request, article_id):
    """
    Adds a comment to a specific article.
    """
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        comment_content = request.POST['comment']
        Comment.objects.create(article=article, author=request.user, content=comment_content)
    return redirect('article_detail', article_id=article_id)
