
# importing django routing libraries
#from django.conf import settings
#from django.conf.urls.static import static
#from django.contrib.sitemaps.views import sitemap
from django.urls import path
from . import views



#from .views import *
#from .feeds import post


 
urlpatterns = [

    # home page
    #path('blog/', views.home, name='home'),
    #path('', views.postslist.as_view(), name='post'),
    # route for posts
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
]

