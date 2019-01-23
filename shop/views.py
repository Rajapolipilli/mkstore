from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Category
from .forms import CartAddProductForm
# from cart.cart import Cart


# Create your views here.
def product_list(request,category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	context = {
		'category':category,
		'categories':categories,
		'products':products
		}
	if category_slug:
		category = get_object_or_404(Category,slug=category_slug)
		products = products.filter(category=category)
		
	return render(request,'pl.html',context)

def product_detail(request,id,slug):
	product = get_object_or_404(Product,id=id,slug=slug,available=True)
	price=product.price
	request.session['id']=product.id
	print(price)
	if request.method == 'POST':
		form = CartAddProductForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			request.session['quantity']=a1=cd['quantity']
			pprice=price*a1
			request.session['pprice']=str(pprice)

			#print("quantity is :",a1)
			return redirect("cart-detail")
	else:
		form = CartAddProductForm()
		return render(request,'detail.html',{'form':form,'product':product})


def cart_details(request):
	id=request.session['id']
	product = get_object_or_404(Product,id=id,available=True)

	cartqty=request.session.get('quantity')
	price=request.session.get('pprice')
	print(product)
	return render(request, 'cart_detail.html', {'cartqty': cartqty,'price':price,'product':product })
