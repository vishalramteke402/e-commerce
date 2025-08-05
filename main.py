# ecommerce_streamlit.py

import streamlit as st

# ----- Product Class -----
class Product:
    def __init__(self, pid, name, price, stock):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} (${self.price}) - Stock: {self.stock}"


# ----- CartItem Class -----
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity


# ----- Cart Class -----
class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.items.append(CartItem(product, quantity))
            product.stock -= quantity
            st.success(f"Added {quantity} x {product.name} to cart.")
        else:
            st.error(f"Only {product.stock} left in stock for {product.name}.")

    def view_cart(self):
        if not self.items:
            st.warning("🛒 Your cart is empty.")
            return

        st.subheader("🛒 Your Cart")
        total = 0
        for item in self.items:
            st.write(f"{item.product.name} x {item.quantity} = ₹{item.get_total_price()}")
            total += item.get_total_price()
        st.success(f"Total: ₹{total}")


# ----- Store Class -----
class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product_by_id(self, pid):
        for p in self.products:
            if p.pid == pid:
                return p
        return None

    def show_products(self):
        st.subheader("🛍️ Available Products")
        for product in self.products:
            st.write(f"**{product.pid}**: {product}")


# ----- Streamlit App -----
def main():
    st.title("🛒 Simple E-Commerce App (OOP + Streamlit)")

    # Initialize store and cart in session_state
    if 'store' not in st.session_state:
        st.session_state.store = Store()
        st.session_state.store.add_product(Product(1, "Laptop", 75000, 5))
        st.session_state.store.add_product(Product(2, "Headphones", 1500, 10))
        st.session_state.store.add_product(Product(3, "Mouse", 700, 15))

    if 'cart' not in st.session_state:
        st.session_state.cart = Cart()

    store = st.session_state.store
    cart = st.session_state.cart

    store.show_products()

    st.markdown("---")
    pid = st.number_input("Enter Product ID", min_value=1, step=1)
    qty = st.number_input("Enter Quantity", min_value=1, step=1)

    if st.button("Add to Cart"):
        product = store.get_product_by_id(pid)
        if product:
            cart.add_to_cart(product, qty)
        else:
            st.error("Invalid product ID.")

    if st.button("View Cart"):
        cart.view_cart()


if __name__ == "__main__":
    main()

