from customers.models import Customer

def create_customer(data):
    try:
        if Customer.objects.filter(username=data["email"]).exists():
            raise ValueError("Conta já criada!")

        customer = Customer.objects.create(
            name=data["name"],
            email=data["email"],
            password=data["password"]
        )
        response = {"id": str(customer.id)}
        return response
    except Exception:
        raise ValueError("erro ao cadastrar!")

def get_customer(data):
    try:
        customer = Customer.objects.get(email=data)
        response = {
            "customer": {
                "email": customer.email,
                "esta_ativo": customer.is_active,
                "total_gasto":customer.total_spend
            }
        }
        return response
    except Exception:
        raise ValueError("Erro no get Customer")
