from django.contrib import admin
from .models import User, Book, Couponcode


class UserAdmin(admin.ModelAdmin):
	fields=["username","phone_number","email_adress","password"]
	list_display= ("id","username","phone_number","email_adress")
admin.site.register(User,UserAdmin)

class BookAdmin(admin.ModelAdmin):
	fields=["book_name","author_name","book_id","book_price"]
	list_display= ("id","book_name","author_name","book_id","book_price")
admin.site.register(Book,BookAdmin)

class CouponcodeAdmin(admin.ModelAdmin):
	fields=["code","discount","is_active","use_count","expiry"]
	list_display= ("id","code","discount","is_active","use_count","expiry")
admin.site.register(Couponcode,CouponcodeAdmin)

