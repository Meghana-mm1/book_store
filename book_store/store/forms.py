from django import forms

class UserForm(forms.Form):
 
    username = forms.CharField(max_length = 100)
    phone_number= forms.CharField(max_length = 100)
    email_adress= forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())


# class Store(forms.Form):
class BookForm(forms.Form):
    book_name=forms.CharField(max_length=100)
    author_name= forms.CharField(max_length=100) 
    book_id =forms.CharField(max_length=100)    


class CouponcodeForm(forms.Form):
    code = forms.CharField(max_length=100)
    use_count= forms.IntegerField()


class OrderForm(forms.Form):
    total_price= forms.IntegerField()
    address= forms.CharField(max_length=100)
    


    