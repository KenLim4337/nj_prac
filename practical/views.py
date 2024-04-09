from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Article, Comment
from datetime import datetime

# Home page displaying list of articles
def home(request):
    # Run autopopulator
    autoPopulator()

    # Log into placeholder account
    user = authenticate(username="testUser", password="password")
    login(request, user)

    return render(request, 'index.html', {
        'articles': Article.objects.all().order_by('pk'),
    })


# # Article details/long form content
# def detail(request, article_id):


# # Add new article page
# def add(request):


# # Edit article page
# def edit(request, article_id):


# # Handle article deletion and redirect
# def delete(request):


# Auto-populate database helper
def autoPopulator():
    # Placeholder user, add if does not already exist
    if (User.objects.filter(username='testUser').count() == 0):
        user = User.objects.create_user('testUser', 'test@test.com', 'password')
        user.first_name = "Test"
        user.last_name = "Testersson"
        user.save()
    else:
        user = User.objects.get(username='testUser')

    # Check if articles already exist, if no seed with lipsum
    if(Article.objects.all().count() == 0):
        
        today = datetime.now()

        # Add 2 articles and 2 comments each
        articles = [
            {
                'title': 'Lorem',
                'thumb': 'https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg',
                'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            },
            {
                'title': 'Ipsum',
                'thumb': 'https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg',
                'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            }
        ]

        comments = {
            'Lorem': {
                'content': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            },
            'Ipsum': {
                'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ',
            }
        }

        for article in articles:
            comment = comments[article['title']]

            newArticle = Article(
                title = article['title'],
                thumb = article['thumb'],
                content = article['content'],
                poster = user,
                posted = today
            )
            newArticle.save()

            newComment = Comment(
                article = newArticle,
                poster = user,
                content = comment['content'],
                posted = today
            )
            newComment.save()
