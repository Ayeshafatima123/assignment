import streamlit as st


class ClothingItem:
    def __init__(self, name, category, price, brand, is_new_arrival=False):
        self.name = name
        self.category = category
        self.price = price
        self.brand = brand
        self.is_new_arrival = is_new_arrival

    def display(self):
        st.subheader(self.name)
        st.text(f"Brand: {self.brand}")
        st.text(f"Category: {self.category}")
        st.text(f"Price: ${self.price}")
        if self.is_new_arrival:
            st.markdown("🆕 **New Arrival**")

class ClothingStore:
    def __init__(self):
        self.items = []

    def add_item(self, item: ClothingItem):
        self.items.append(item)

    def show_all_items(self):
        st.header("🛍️ All Clothing Items")
        for item in self.items:
            item.display()
            st.markdown("---")

    def show_new_arrivals(self):
        st.header("✨ New Arrivals")
        for item in self.items:
            if item.is_new_arrival:
                item.display()
                st.markdown("---")

    def show_by_brand(self, brand_name):
        st.header(f"🧥 Items by Brand: {brand_name}")
        for item in self.items:
            if item.brand.lower() == brand_name.lower():
                item.display()
                st.markdown("---")



store = ClothingStore()

# Add Sample Items
store.add_item(ClothingItem("Classic Black Suit", "Suit", 299.99, "Zegna", is_new_arrival=True))
store.add_item(ClothingItem("Slim Fit Navy Suit", "Suit", 249.99, "Armani"))
store.add_item(ClothingItem("Casual T-Shirt", "Top", 49.99, "Nike", is_new_arrival=True))
store.add_item(ClothingItem("Sport Jacket", "Outerwear", 199.99, "Adidas"))


st.title("👗 Clothing Sales App")

menu = st.sidebar.selectbox("Choose View", ["All Items", "New Arrivals", "By Brand"])
if menu == "All Items":
    store.show_all_items()
elif menu == "New Arrivals":
    store.show_new_arrivals()
elif menu == "By Brand":
    selected_brand = st.sidebar.text_input("Enter Brand Name")
    if selected_brand:
        store.show_by_brand(selected_brand)



class ClothingItem:
    def __init__(self, name, clothing_type, size):
        self.name = name
        self.clothing_type = clothing_type
        self.size = size

    def __str__(self):
        return f"{self.name} - {self.clothing_type} - Size {self.size}"

class ClothesInventory:
    def __init__(self):
        if 'clothes' not in st.session_state:
            st.session_state.clothes = []

    def add_item(self, name, clothing_type, size):
        item = ClothingItem(name, clothing_type, size)
        st.session_state.clothes.append(item)

    def get_all_items(self):
        return st.session_state.clothes

    def filter_items(self, clothing_type=None, size=None):
        items = self.get_all_items()
        if clothing_type:
            items = [item for item in items if item.clothing_type == clothing_type]
        if size:
            items = [item for item in items if item.size == size]
        return items

class ClothesApp:
    def __init__(self):
        self.inventory = ClothesInventory()

    def run(self):
        st.title("👕 Clothes Inventory App")

        st.subheader("➕ Add New Clothing Item")
        name = st.text_input("Name")
        clothing_type = st.selectbox("Type", ["Shirt", "Pants", "Jacket", "Shoes"])
        size = st.selectbox("Size", ["S", "M", "L", "XL"])

        if st.button("Add Item"):
            if name:
                self.inventory.add_item(name, clothing_type, size)
                st.success("Item added!")
            else:
                st.warning("Please enter a name.")

        st.subheader("🔍 Filter Inventory")
        filter_type = st.selectbox("Filter by Type", ["All", "Shirt", "Pants", "Jacket", "Shoes"])
        filter_size = st.selectbox("Filter by Size", ["All", "S", "M", "L", "XL"])

        st.subheader("📦 Clothes List")
        filtered_items = self.inventory.filter_items(
            clothing_type=None if filter_type == "All" else filter_type,
            size=None if filter_size == "All" else filter_size
        )

        if filtered_items:
            for item in filtered_items:
                st.write(str(item))
        else:
            st.info("No items match your filter.")

if __name__ == "__main__":
    app = ClothesApp()
    app.run()
