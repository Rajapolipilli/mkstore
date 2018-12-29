from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Category
from cart.forms import CartAddProductForm
from cart.cart import Cart


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

	# return render(request,'detail.html',{'product':product})
	cart = Cart(request)
	if request.method == 'POST':
		form = CartAddProductForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'])
			return redirect('cart:cart_detail')
	else:
		form = CartAddProductForm()
		return render(request,'detail.html',{'form':form,'product':product})


# def cart_add(request, product_id):
    
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     return redirect('cart:cart_detail')
