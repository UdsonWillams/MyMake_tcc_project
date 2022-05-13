
from cart.models import Carts
from products.models import Products

def devoluting_products(data):
    devoluting = False
    try:
        cart = Carts.objects.get(customer_id=data["pk"])
        for i in range(0, len(cart.products.all())):
            product = cart.products.all()[i]            
            new_quantity = product.quantity + product.cart_quantity
            Products.objects.filter(pk=product.id).update(quantity=new_quantity)
        cart.delete()
        devoluting = True
    except Exception:
        raise ValueError
    return devoluting

def actualize_cart(url, body):
    is_actualize = False
    try:
        cart = Carts.objects.get(customer_id=url["pk"])
        new_products_list = body["products"]
        cart_products = cart.products.all()
        for v in range(len(cart.products.all())):            
            new_products = cart.products.all()[v].id
            product = Products.objects.get(name=body["products"][i]["name"])
            cart_quantity = body["products"][i]["cart_quantity"]            
            if product.id == new_products:
                product.update(cart_quantity=product.cart_quantity + cart_quantity)              
        cart.products.add(product)
        cart.save()
        is_actualize = True
    except Exception:
        raise ValueError
    return is_actualize

def finalize_cart(data):
    try:
        cart = Carts.objects.get(customer_id=data["pk"])
        cart.delete()
        devoluting = {"status": "sucess","message": "estamos lhe encaminhando para pagina de pagamento"}
    except Exception:
        raise ValueError
    return devoluting
