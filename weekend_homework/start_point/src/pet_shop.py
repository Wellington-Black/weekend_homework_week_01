# WRITE YOUR FUNCTIONS HERE
customers = [
    {
        "name": "Alice",
        "pets": [],
        "cash": 1000
    },
    {
        "name": "Bob",
        "pets": [],
        "cash": 50
    },
    {
        "name": "Jack",
        "pets": [],
        "cash": 100
    }
]

new_pet = {
    "name": "Bors the Younger",
    "pet_type": "cat",
    "breed": "Cornish Rex",
    "price": 100
}

pet_shop = {
    "pets": [
        {
            "name": "Sir Percy",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "King Bagdemagus",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "Sir Lancelot",
            "pet_type": "dog",
            "breed": "Pomsky",
            "price": 1000,
        },
        {
            "name": "Arthur",
            "pet_type": "dog",
            "breed": "Husky",
            "price": 900,
        },
        {
            "name": "Tristan",
            "pet_type": "cat",
            "breed": "Basset Hound",
            "price": 800,
        },
        {
            "name": "Merlin",
            "pet_type": "cat",
            "breed": "Egyptian Mau",
            "price": 1500,
        }
    ],
    "admin": {
        "total_cash": 1000,
        "pets_sold": 0,
    },
    "name": "Camelot of Pets"
}


def get_pet_shop_name(pet_shop):
    name = pet_shop["name"]
    return name

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]
    

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    cash = pet_shop["admin"]["total_cash"]
    return cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets):
    pet_shop["admin"]["pets_sold"] += pets
    return pet_shop["admin"]["pets_sold"]

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets = []
    for animal in pet_shop["pets"]:
        if animal["breed"] == breed:
            pets.append(breed)
    return pets

def find_pet_by_name(pet_shop, name):
    for animal in pet_shop["pets"]:
        if animal["name"] == name:
            return animal

def remove_pet_by_name(pet_shop, name):
    pet = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    count = pet_shop["pets"].append(new_pet)
    return count

def get_customer_cash(customer):
    for client in customers:
        if client["name"] == customer["name"]:
            return customer["cash"]

def remove_customer_cash(customer, amount):
    for client in customers:
        if client["name"] == customer["name"]:
            customer["cash"] -= amount

def get_customer_pet_count(customer):
    for client in customers:
        if client["name"] == customer["name"]:
            return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    for client in customers:
        if client["name"] == customer["name"]:
            customer["pets"].append(new_pet)
    return len(customer["pets"])

def customer_can_afford_pet(customer, new_pet):
    for client in customers:
        return client["name"] == customer["name"] and client["cash"] >= new_pet["price"]
    
# def customer_can_afford_pet(customer, new_pet):
#     for client in customers:
#         return client["name"] == customer["name"] and client["cash"] == new_pet["price"]