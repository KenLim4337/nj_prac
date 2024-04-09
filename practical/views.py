from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Article, Comment

# # Home page displaying list of articles
# def home(request):
#     userData = None
    
#     # Always log into the first available user
#     if request.session.get('userid', None) != None:
#         userData = {

#         }

#     return render(request, 'coviDash/home.html', {
#         'rumours': Article.objects.all().order_by('pk'),
#         'userData': userData,
#     })


# # Article details/long form content
# def detail(request, article_id):


# # Add new article page
# def add(request):


# # Edit article page
# def edit(request, article_id):


# # Handle article deletion and redirect
# def delete(request):