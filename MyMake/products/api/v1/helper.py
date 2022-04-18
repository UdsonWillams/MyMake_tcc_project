from products.models import Products


def get_product(name):
    try:
        product = Products.objects.get(name=name)
    except Exception:
        raise ValueError()
    
    return {
    "id": product.id,
    "name": product.name,
    "price": product.price,
    "description": product.description,
    "quantity": product.quantity,
    }
