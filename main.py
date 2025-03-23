from product import Product
from employee import Employee
from user import User


products = [
        Product("Laptop", 2000, 15, "High-end laptop"),
        Product("Phone", 800, 20, "Smartphone"),
        Product("Tablet", 500, 25, "Android tablet"),
        Product("Headphones", 150, 30, "Noise-cancelling headphones"),
        Product("Monitor", 350, 12, "27-inch monitor")
    ]

    # Angajați
employees = [
        Employee("Alice Johnson", "alice.johnson@example.com", 3000, "123 Main St"),
        Employee("Bob Smith", "bob.smith@example.com", 4000, "456 Oak St")
    ]

    # Utilizatori
users = [
        User("John Doe", "johndoe123", "123-456-7890", "789 Pine St"),
        User("Jane Doe", "janedoe456", "098-765-4321", "321 Elm St"),
        User("James Bond", "james.bond007", "555-1234", "007 London St")
    ]

    # Adăugăm produse în istoricul utilizatorilor
users[0].add_product(products[0])
users[0].add_product(products[2])
users[1].add_product(products[1])
users[1].add_product(products[3])
users[2].add_product(products[4])

    # Afișăm informațiile utilizatorilor și angajaților
for user in users:
    print(user.display_info())
    
for employee in employees:
    print(employee.display_info())