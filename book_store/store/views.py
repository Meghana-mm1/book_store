from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm,BookForm,CouponcodeForm
from .models import User,Book,Couponcode


TEMPLATES_DIRS =(
	'os.path.join(BASE_DIR, "templates"),')




def index(request):
	context ={}
	context["name"]="Meghna"
	context["Email_adress"]= "megha@gmail.com"
	print(f'16-------------{context}')
	return render(request,"index.html", context)
# Create your views here.


def user_form(request):
	# print(f'23-------------{request.__dict__}')
	if request.method=='POST':
		# print(f'25-------------{request}')
		username=request.POST.get('username')
		# print(f'27-------------{request}')
		phone_number=request.POST.get('phone_number')
		# print(f'29-------------{request}')
		email_adress=request.POST.get('email_adress')
		# print(f'31-------------{request}')
		password=request.POST.get('password')
		# print(f'33-------------{request}')
		print(f'28-------{username}------{phone_number}-----------{email_adress}------{password}-----')
		user=User.objects.create(username=username,phone_number=phone_number,email_adress=email_adress,password=password)
		# messages.success(request,'Data has been submitted')
	context ={}
	context['form']= UserForm()
	return render(request, "home.html", context)


def book_form(request):
	if request.method=='POST':
		book_name=request.POST.get('book_name')
		author_name=request.POST.get('author_name')
		book_id=request.POST.get('book_id')
		print(f'28-------{book_name}------{author_name}-----------{book_id}----------')
		book=Book.objects.create(book_name=book_name,author_name=author_name,book_id=book_id)
		context ={}
		context["book_name"]=book_name
		context["author_name"]=author_name
		context["book_id"]=book_id
		return render(request, "booklist.html", context)
		# return HttpResponse("book details updated sucessfully")
	# messages.success(request,'Data has been submitted')
	context ={}
	context['form']= BookForm()
	return render(request, "home.html", context)


def Couponcode_form(request):
	if request.method=='POST':
		code=request.POST.get('code')
		use_count=request.POST.get('use_count')
		print(f'67-------{code}------{use_count}------------------')
		couponcode=Couponcode_form.objects.create(code=code,use_count=use_count)
		context={}
		context['form']= Couponcodeform()
		return render(request, "mmm.html", context)

def book_list(request):
	book_list = Book.objects.all()
	couponcode_obj= Couponcode.objects.last()
	context = {
		"book_list": book_list,
		"couponcode_obj":couponcode_obj
	}
	print(f'77-------{book_list}----------')
  
	return render(request,"table.html",context)





def buy_book(request, *args, **kwargs):
	lst=kwargs["slug"].split("_")
	obj = Book.objects.get(pk=int(lst[0]))
	x=type(obj)
	coupon_obj= Couponcode.objects.get(pk=int(lst[1]))
	y=type(coupon_obj)
	print(f'97--------------{obj.__dict__}')
	print(f'98--------------{coupon_obj.__dict__}')
	print(x)
	b_price=obj.book_price
	b_discount=coupon_obj.discount
	discounted_price = b_price - (b_price * b_discount / 100)

	context={"discounted_price":discounted_price,
	  "book_name":obj.book_name,
	  "code":coupon_obj.code,
	  "discount":coupon_obj.discount}
	return render(request,"price_show.html",context)



def order_view(request):
	if request.method=='POST':
		book=request.POST.get('book')
		total_price=request.POST.get('total_price')
		address=request.POST.get('adresss')

		print(f'67------{book}------{total_price}------{address}------------')
		order=Order_form.objects.create(book=book,total_price=total_price,address=address)
		
	return render(request,"order.html")













