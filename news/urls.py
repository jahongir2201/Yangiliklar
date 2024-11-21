from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import category, region, all_region, all_category, Create_post, all_news, home, detail, Edit_Post, \
    Delete_Post



urlpatterns = [
    path('', home, name='home'),
    path('all-news', all_news, name='all_news'),
    path('detail/<int:id>', detail, name='detail'),
    path('category/<int:id>', category, name='category'),
    path('all-categories', all_category, name='all-category'),
    path('region/<int:id>', region, name='region'),
    path('all-regions', all_region, name='all-region'),
    path('create-post/new', Create_post.as_view(), name='create-post'),
    path('edit_post/<int:pk>/edit', Edit_Post.as_view(), name='editpost'),
    path('delete_post/<int:pk>/delete', Delete_Post.as_view(), name='deletepost'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)