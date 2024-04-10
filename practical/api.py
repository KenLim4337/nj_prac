from django.http import JsonResponse
from .models import Article, Comment
from datetime import datetime


def get_article(request, article_id):
    id = article_id
    
    article = Article.objects.filter(pk=id)

    json_data = {}

    if (article.count() > 0):
        article = article[0]
        
        comments = Comment.objects.filter(article=article)

        json_data = {
            'id': article.id,
            'title': article.title,
            'thumbnail': article.thumb,
            'content': article.content,
            'poster': article.poster.username,
            'posted': article.posted,
            'comments': [],
            'status': 'success',
        }

        temp_comments = []

        for comment in comments: 
            temp_comments.append({
                'poster': comment.poster.username,
                'content': comment.content,
                'posted': comment.posted
            })

        
        json_data['comments'] = temp_comments
    else:
        json_data = {
            'status': 'failure',
        }
    
    return JsonResponse(json_data)


def add_article(request):
    json_data = {}

    new_article = Article(
        title = request.POST.get('title'),
        thumb = request.POST.get('thumbnail'),
        content = request.POST.get('content'),
        poster = request.user,
        posted = datetime.now()
    )

    new_article.save()

    json_data = {
        'article': {
            'id': new_article.id,
            'title': new_article.title,
            'thumb': new_article.thumb,
            'content': new_article.content,
            'poster': new_article.poster.username,
            'posted': new_article.posted.strftime("%B %d, %Y, %I:%M %p"),
        },
        'status': 'success',
    }

    return JsonResponse(json_data)


def remove_article(request, article_id):
    id = article_id
    
    article = Article.objects.filter(pk=id)

    json_data = {}

    if (article.count() > 0):
        article[0].delete()

        json_data = {
            'id': id,
            'status': 'success',
        }
    else:
        json_data = {
            'id': id,
            'status': 'failure',
        }
    
    return JsonResponse(json_data)


def edit_article(request, article_id):
    target_article = Article.objects.filter(pk=article_id)[0]

    title = request.POST.get('title')
    thumb = request.POST.get('thumbnail')
    content = request.POST.get('content')

    target_article.title = title
    target_article.thumb = thumb
    target_article.content = content

    target_article.save()

    json_data = {
        'article': {
            'id': target_article.id,
            'title': target_article.title,
            'thumb': target_article.thumb,
            'content': target_article.content,
            'poster': target_article.poster.username
        },
        'status': 'success', 
    }

    return JsonResponse(json_data)



    
def add_comment(request, article_id):
    json_data = {}

    targetArticle = Article.objects.filter(pk=article_id)[0]

    new_comment = Comment(
        article = targetArticle,
        content = request.POST.get('content'),
        poster = request.user,
        posted = datetime.now()
    )

    new_comment.save()

    json_data = {
        'comment': {
            'content': new_comment.content,
            'poster': new_comment.poster.username,
        },
        'status': 'success',
    }

    return JsonResponse(json_data)
