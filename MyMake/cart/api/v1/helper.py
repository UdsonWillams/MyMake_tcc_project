from cart.models import Carts
from products.models import Products

def devoluting_products(data):
    devoluting = False
    try:
        cart = Carts.objects.get(id=data["pk"])
        products = cart.products
        new_quantity = products.quantity + cart.quantity
        Products.objects.filter(pk=products.id).update(quantity=new_quantity)
        cart.delete()
        devoluting = True
    except Exception:
        raise ValueError
    return devoluting

def actualize_cart(url, body):
    import ipdb
    ipdb.set_trace()
    is_actualize = False
    try:
        cart = Carts.objects.get(id=url["pk"])
        corpo = body["products"]
        for value in corpo:
            for name in cart.products:
                if value["name"] == name["name"]:
                    is_actualize = False
                    return is_actualize
        cart.products.append(body["products"])
        cart.save()
        is_actualize = True
    except Exception:
        raise ValueError
    return is_actualize
