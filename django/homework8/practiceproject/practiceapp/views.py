from django.shortcuts import redirect, render
from slugify import slugify
from practiceapp.models import Store, Category, Product

# Create your views here.
def view(req):
    search = req.GET.get('search') or ''
    stores = Store.objects.filter(name__icontains=search)
    ctx = {
        'stores':stores
    }
    return render(req, 'practiceapp/index.html', ctx)

def add_store(req):
    if req.POST.get('store_name'):
        store = Store()
        store.name = req.POST.get('store_name')
        store.slug = slugify(store.name)
        store.save()
    return redirect('index')

def store_info(req, store_slug):
    search = req.GET.get('search') or ''
    categories = Category.objects.filter(name__icontains=search)
    store = Store.objects.get(slug=store_slug)
    ctx = {
        'categories': categories,
        'store': store
    }
    return render(req, 'practiceapp/stores.html', ctx)

def add_cat(req):
    store = req.POST.get('store_slug')
    if req.POST.get('cat_name'):
        cat = Category()
        cat.name = req.POST.get('cat_name')
        cat.slug = slugify(cat.name)
        cat.save()
    return redirect(f'store/{store}')

def products(req, cat_slug, store_slug):
    search = req.GET.get('search') or ''
    category = Category.objects.get(slug=cat_slug)
    store = Store.objects.get(slug=store_slug)
    products = store.products.filter(category_id=category.id, name__icontains=search)
    ctx = {
        'category':category,
        'store':store,
        'products':products
    }
    return render(req, 'practiceapp/products.html', ctx)

def add_prod(req):
    store = Store.objects.get(slug=req.POST.get('store_slug'))
    category = Category.objects.get(id=req.POST.get('cat_id'))
    if req.POST.get('product_name'):
        product = Product()
        product.name = req.POST.get('product_name')
        product.category = category
        product.slug = slugify(product.name)
        product.price = req.POST.get('product_price')
        product.save()
        store.products.add(product)
        store.save()
    return redirect(f'products/{category.slug}/{store.slug}')

def edit_prod(req):
    store = req.POST.get('store_slug')
    cat = req.POST.get('cat_slug')
    product = Product.objects.get(id=req.POST.get('product_id'))
    product.name = req.POST.get('product_name')
    product.price = req.POST.get('product_price')
    product.save()
    return redirect(f'products/{cat}/{store}')

def del_prod(req):
    product = Product.objects.get(id=req.GET.get('prod_id'))
    product.delete()
    cat = req.GET.get('cat')
    store = req.GET.get('store')
    return redirect(f'products/{cat}/{store}')
