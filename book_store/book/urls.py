from django.urls import path
from book.views import home,store_book,show_books,edit_book,delete_book

urlpatterns = [
      
      path('',home),
      path('store_new_book/',store_book,name='storebook'),
      path('show_books/',show_books,name='showbooks'),
      path('edit_books/<int:id>',edit_book,name='editbook'),
      path('delete_book/<int:id>',delete_book,name='delete_book'),
]