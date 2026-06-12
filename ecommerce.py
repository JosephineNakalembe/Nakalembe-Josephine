# Step 1: Define user accounts
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "customer": {"password": "cust123", "role": "Customer"},
    "cashier": {"password": "cash123", "role": "Cashier"}
}

# Step 2: Login system
username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username]["password"] == password:
    role = users[username]["role"]
    print(f"Login successful! Welcome {role}.")
else:
    print("Invalid credentials. Access denied.")
    exit()

# Step 3: Shopping system
subtotal = float(input("Enter subtotal: "))
coupon = input("Enter coupon code (or press Enter if none): ")
location = input("Enter location (urban/rural): ")

# Step 4: Nested conditionals for coupon and tax
discount = 0
if coupon == "SAVE10":
    discount = 0.10
elif coupon == "SAVE20":
    discount = 0.20
else:
    print("Invalid or no coupon applied.")

# Tax rate based on location
if location.lower() == "urban":
    tax_rate = 0.18
elif location.lower() == "rural":
    tax_rate = 0.10
else:
    tax_rate = 0.15  # default

# Step 5: Calculate final price
discount_amount = subtotal * discount
tax_amount = (subtotal - discount_amount) * tax_rate
final_price = subtotal - discount_amount + tax_amount

print("\n--- Receipt ---")
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount_amount}")
print(f"Tax: {tax_amount}")
print(f"Final Price: {final_price}")