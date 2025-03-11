from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse

class AdminRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Define admin restricted paths
        # admin_paths = ['/add_product/', '/product_edit/']

        # Check if the user is trying to access admin restricted paths
        if request.path.startswith('/add_product/') or request.path.startswith('/product_edit/'):
            if not request.user.is_superuser:
                return redirect('error')  # Redirect to the error page

        return None  # Allow the request to proceed
