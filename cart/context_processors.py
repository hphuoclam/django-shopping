from .cart import Cart
from django.conf import settings

def cart(request):
    print('-------------')
    print(request.LANGUAGE_CODE)
    return {
        'cart': Cart(request),
        'LANGUAGES': settings.LANGUAGES,
        'SELECTEDLANG':request.LANGUAGE_CODE
    }

