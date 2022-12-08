# DEF FOR EACH MENU OPTION
customer = ''

def add_customer(customer,name,lastname,id):
    customer = {}
    customer['name'] = name
    customer['last name'] = lastname
    customer['id'] = id
    customer.append(customer)

def show_customer(customer):
    for i in customer:
        print(f"Name: {i['name']}, Last name: {i['lastname']}, Id: {i['is']}")

def show_customer(customer,id):
    for i in customer:
        if i['id'] == id:
            print(f"Name: {i['name']}, Last name: {i['lastname']}, Id: {i['is']}")
            return True
    return False

def delete_customer(customer,id):
    for i in customer:
        if i['id'] == id:
            customer.remove(i)
            return True
    return False

clientes = [] # make a LIST

while True:
    print("""\t.:MENU:.
1. add new customer
2. show all customer
3. show customer by id
4. delete customer
5. Exit""")
    option = int(input("Typer an option: "))

    print()

    if option==1:
        name = input("customer name -> ")
        lastname = input("customer last name -> ")
        dni = input("customer id -> ")
        add_customer(customer,name,lastname,id)

    elif option==2:
        show_customer(clientes)

    elif option==3:
        id = input("customer ID -> ")
        if show_customer(customer,id):
            print("customer found")
        else:
            print("not found")

    elif option==4:
        id = input("customer ID -> ")
        if delete_customer(customer,id):
            print("customer deleted")
        else:
            print("not found")

    elif option==5:
        break

    else:
        print("error, Type you option again")

    print()