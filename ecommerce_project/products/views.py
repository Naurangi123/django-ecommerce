from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect
from .models import Product,Review
from orders.models import Cart, CartItem
from .forms import ProductForm,ReviewForm
from django.contrib.auth.decorators import login_required,user_passes_test

def search(request):
    q = request.GET.get('q', None)
    product = ""
    if q is None or q is "":
        product = Product.objects.all()   
    product = Product.objects.filter(title__contains=q)
    return render(request, 'users/search.html', {'product': product })

def error(request):
    return render(request,'products/error.html')

@login_required
def add_product(request):
    
    form=ProductForm()
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form=ProductForm()
    return render(request,'products/add_product.html',{'form':form})
        
    
def products(request):
    products=Product.objects.all().order_by('-id')
    context={
        'products':products,
    }
    return render(request,'products/index.html',context)

def product_details(request, id):
    try:
        product = Product.objects.get(id=id)
        review = product.reviews.all()  # Get all reviews for this product
        form = ReviewForm()  
        
    except Product.DoesNotExist:
        return redirect('products') 


    context = {
        'product': product,
        'category': product.category,
        'reviews':review,
        'form':form,
    }
    return render(request, 'products/product_details.html', context)
# @login_required
# @user_passes_test(is_admin)
def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    
    # if not is_admin(request.user):
    #     return redirect('error')
    
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/product_edit.html', {'form': form,'product':product})
    
    
@login_required
def add_review(request, id):
    product = get_object_or_404(Product, id=id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been submitted!')
            return redirect('product_details', id=product.id)
    
    return redirect('product_details', id=product.id)

# Cart Fuction
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
    cart_item.save()
    if item_created:
        messages.success(request, f'{product.name} has been added to your cart.')
    else:
        messages.info(request, f'The quantity of {product.name} in your cart has been updated.')
    return redirect('cart_detail')


@login_required
def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            item.total_price = item.quantity * item.product.price
    else:
        cart_items = []
    context = {
        'cart_items': cart_items
    }
    return render(request, 'products/cart_detail.html', context)

@login_required
def delete_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.delete()
        messages.success(request, f'{product.name} has been removed from your cart.')
    except CartItem.DoesNotExist:
        messages.warning(request, f'{product.name} was not found in your cart.')
        
    return redirect('cart_detail')



@login_required
def edit_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)

    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity'))

        if new_quantity > 0:
            cart_item.quantity = new_quantity
            cart_item.save()
            messages.success(request, f'The quantity of {cart_item.product.name} has been updated.')
        else:
            cart_item.delete()
            messages.success(request, f'{cart_item.product.name} has been removed from your cart.')

    return redirect('cart_detail')