from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

ITEM_PER_PAGE = 6

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    paginator = Paginator(products, ITEM_PER_PAGE)
    page = request.GET.get('page')
    products_list = paginator.get_page(page)

    context = {
        'category': category,
        'categories': categories,
        'products': products_list,
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, slug, id):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

