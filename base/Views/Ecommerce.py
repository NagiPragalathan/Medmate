from django.shortcuts import render, redirect
from base.models import EProduct


def add_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        product_type = request.POST.get('product_type')
        price = request.POST.get('price')
        product_image = request.FILES.get('product_image')

        product = EProduct(
            product_name=product_name,
            description=description,
            product_type=product_type,
            price=price,
            product_image=product_image
        )
        product.save()
        return redirect('list_products')
    return render(request, 'Product/add_product.html')



def list_products(request):
    products = EProduct.objects.all()
    return render(request, 'Product/list_products.html', {'products': products})


def edit_product(request, id):
    product = EProduct.objects.get(id=id)
    if request.method == 'POST':
        product.product_name = request.POST.get('product_name', product.product_name)
        product.description = request.POST.get('description', product.description)
        product.product_type = request.POST.get('product_type', product.product_type)
        product.price = request.POST.get('price', product.price)
        if 'product_image' in request.FILES:
            product.product_image = request.FILES['product_image']
        product.save()
        return redirect('list_products')
    return render(request, 'Product/edit_product.html', {'product': product})



def delete_product(request, id):
    product = EProduct.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('list_products')
    return render(request, 'Product/confirm_delete_product.html', {'product': product})
