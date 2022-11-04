from django.db import models


   
 

class User(models.Model):
	username = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100)
	email_adress= models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id) +"----"+ self.username

class Book(models.Model):
	book_name=models.CharField(max_length=100)
	author_name= models.CharField(max_length=100) 
	book_id =models.CharField(max_length=100)
	book_price=models.IntegerField(default=1) 

	def __int__(self):
		return str(self.id)


class Store(models.Model):
	name = models.CharField(max_length=100)
	owner = models.CharField(max_length=100)
	is_active= models.BooleanField(default=True)
	book= models.ManyToManyField(Book,blank=True,null=True)
	
	def __str__(self):
		return str(self.id)


class Couponcode(models.Model):
	code = models.CharField(max_length=100)
	discount= models.IntegerField(blank=True,null=True)
	is_active= models.BooleanField(default=True)
	use_count= models.IntegerField(default=0)
	expiry= models.DateTimeField(blank=True,null=True)
	
	
	def __str__(self):
		return str(self.discount)+"%---"+str(self.id)


# class Order
# book, total price, address, is_deliverd,
class Order(models.Model):
	book= models.ManyToManyField(Book,blank=True,null=True)
	total_price= models.IntegerField(blank=True,null=True)
	address= models.CharField(max_length=100)
	is_delivered= models.BooleanField(default=True)
	











# Create your models here.
