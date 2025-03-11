from django.shortcuts import redirect,render




def checkout(request):
    
    return render(request,'orders/checkout.html')



def order_summery(request):
    
    return render(request,'orders/order_summery.html')