
class Product:
    def __init__(self, pid, name, price, stock):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} (${self.price}) - Stock: {self.stock}"


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity


class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.items.append(CartItem(product, quantity))
            product.stock -= quantity
            print(f"Added {quantity} x {product.name} to cart.")
        else:
            print(f"Sorry, only {product.stock} left in stock for {product.name}.")

    def view_cart(self):
        print("\n🛒 Your Cart:")
        if not self.items:
            print("Cart is empty.")
            return
        for item in self.items:
            print(f"{item.product.name} x {item.quantity} = ${item.get_total_price()}")
        print(f"Total: ${self.calculate_total()}")

    def calculate_total(self):
        return sum(item.get_total_price() for item in self.items)


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print("\n🛍️ Available Products:")
        for product in self.products:
            print(f"{product.pid}: {product}")


# Demo / Main
def main():
    store = Store()
    # Adding sample products
    store.add_product(Product(1, "Laptop", 75000, 5))
    store.add_product(Product(2, "Headphones", 1500, 10))
    store.add_product(Product(3, "Mouse", 700, 15))

    cart = Cart()

    while True:
        store.show_products()
        choice = input("\nEnter product ID to add to cart (or 'checkout' to finish): ")

        if choice.lower() == 'checkout':
            break

        try:
            pid = int(choice)
            product = next((p for p in store.products if p.pid == pid), None)

            if not product:
                print("Invalid product ID.")
                continue

            qty = int(input(f"Enter quantity for {product.name}: "))
            cart.add_to_cart(product, qty)

        except ValueError:
            print("Invalid input. Please try again.")

    cart.view_cart()
    print("\n✅ Thank you for shopping!")

if __name__ == "__main__":
    main()
