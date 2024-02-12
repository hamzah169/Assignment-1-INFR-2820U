
import time

# Task 1: Load and Store Data ----------------------------------------------------------------------------------------------------------
def load_product_data(file_name):
    products = []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            product_id = int(parts[0])
            name = parts[1]
            price = float(parts[2])
            category = parts[3]
            products.append({'product_id': product_id, 'name': name, 'price': price, 'category': category})
    return products

# Task 2: Data Manipulation Operations ----------------------------------------------------------------------------------------------------------

# Function to find a product by its ID
def find_product_by_id(products, product_id):
    for product in products:
        if product['product_id'] == product_id:
            return product
    return None

# Function to insert a new product
def insert_product(products, product_id, name, price, category):
    if find_product_by_id(products, product_id) is None:
        products.append({'product_id': product_id, 'name': name, 'price': price, 'category': category})
        print(f"Product with ID {product_id} inserted")
    else:
        print(f"Product with ID {product_id} already exists.")

# Function to update an existing product
def update_product(products, product_id, name, price, category):
    for product in products:
        if product['product_id'] == product_id:
            product['name'] = name
            product['price'] = price
            product['category'] = category
            print(f"Product with ID {product_id} updated")
            return
    print(f"Product with ID {product_id} does not exist.")

# Function to delete a product
def delete_product(products, product_id):
    for i, product in enumerate(products):
        if product['product_id'] == product_id:
            del products[i]
            print(f"Product with ID {product_id} deleted")
            return
    print(f"Product with ID {product_id} does not exist.")

# Function which displays products
def display_products(products):
    for product in products:
        print(f"Product ID: {product['product_id']}, Name: {product['name']}, Price: {product['price']}, Category: {product['category']}")

# Function to search for a product by ID
def search_product_by_id(products, product_id):
    product = find_product_by_id(products, product_id)
    if product:
        print(f"Product ID: {product['product_id']}, Name: {product['name']}, Price: {product['price']}, Category: {product['category']} SEARCHED")
    else:
        print(f"Product with ID {product_id} does not exist.")

# Task 3: Sorting Algorithm Implementation ----------------------------------------------------------------------------------------------------------

# Function which does bubble sort based off price
def bubble_sort_by_price(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n-i-1):
            if products[j]['price'] > products[j+1]['price']:
                products[j], products[j+1] = products[j+1], products[j]
    return products

# Function which generates sorted data
def generate_sorted_data(size):
    return [{'product_id': i, 'name': f'Product {i}', 'price': i, 'category': 'Category'} for i in range(1, size + 1)]

# Function which generates reverse-sorted data
def generate_reverse_sorted_data(size):
    return [{'product_id': i, 'name': f'Product {i}', 'price': size - i + 1, 'category': 'Category'} for i in range(1, size + 1)]

# Function to record and compare sorting time
def compare_sorting_time(data_generator, size, sorting_function):
    data = data_generator(size)
    start_time = time.time()
    sorted_data = sorting_function(data)
    end_time = time.time()
    return end_time - start_time

# Main function
if __name__ == "__main__":
    # Load data into an array
    product_data = load_product_data('product_data.txt')
    print("Product Data Loaded!")

    # Insert a new product
    insert_product(product_data, 99999, 'New Product', 99.99, 'Electronics')

    # Update an existing product
    update_product(product_data, 99999, 'Updated Product', 199.99, 'Electronics')

    # Delete a product
    delete_product(product_data, 99999)

    # Display products
    print("\nCurrent Product Data:")
    display_products(product_data)

    # Search for a product by ID
    search_product_by_id(product_data, 57353)

    # Using the sorting algorithm
    sorted_products = bubble_sort_by_price(product_data)
    print("\nProduct Data Sorted By Price:")
    display_products(sorted_products)

    num_products = len(product_data)

    # Compare sorting time for sorted and reverse-sorted data
    sizes = [num_products, 1000, 5000]  # Sizes of data to test

    for size in sizes:
        print(f"\nSize of data: {size}")
        # Sorted data
        sorted_time = compare_sorting_time(generate_sorted_data, size, bubble_sort_by_price)
        print(f"Time taken to sort sorted data: {sorted_time:.6f} seconds")

        # Reverse-sorted data
        reverse_sorted_time = compare_sorting_time(generate_reverse_sorted_data, size, bubble_sort_by_price)
        print(f"Time taken to sort reverse-sorted data: {reverse_sorted_time:.6f} seconds\n")