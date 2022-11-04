from django.urls import path
from.import views
urlpatterns = [
    path("",views.index,name="index"),
    path("user/form",views.user_form,name="user-form"),
    path("book/form",views.book_form,name="book-form"),
    path("couponcode/form",views.book_form,name="couponcode-form"),
    path("book/list",views.book_list,name="book/list"),
    path("book/buy/<slug>",views.buy_book,name="book-id"),
    path("book/buy/<slug>",views.buy_book,name="book-id"),
    path("book/order",views.order_view)

    

    

]