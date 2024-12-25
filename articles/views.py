from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

def home(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'index.html', context)

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        author = request.POST.get('author')

        if all([title, category, short_content, long_content, author]):
            Article.objects.create(
                title=title,
                category=category,
                short_content=short_content,
                long_content=long_content,
                author=author,
            )
            return redirect('home')

    return render(request, 'articles/add-post.html')

def article_category(request, category):
    articles = Article.objects.filter(category=category)
    context = {
        'articles': articles,
        'category': category,
    }
    return render(request, 'articles/articles-by-category.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)
