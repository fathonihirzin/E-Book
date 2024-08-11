from django.urls import path

from .views import index_view, detail_view, create_view, update_view, delete_view

app_name = 'ebook'
urlpatterns = [
    path('', index_view, name='index'),

    path('<int:ebook_id>', detail_view, name='detail'),

    path('create', create_view, name='create'),

    path('update/<int:ebook_id>', update_view, name='update'),

    path('delete/<int:ebook_id>', delete_view, name='delete'),
]