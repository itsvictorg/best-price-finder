import tkinter as tk
import requests

# Function to get the lowest price from Google Shopping
def get_lowest_price():
    model_number = model_entry.get()

    # Construct the SerpApi URL
    serpapi_url = f"https://serpapi.com/search.json?engine=google_shopping&q={model_number}&api_key=90ded0444765a3e638fc35e5236d76b7a513fe0f563f97e3618ebf12aebc1282"

    # Send a GET request to SerpApi
    response = requests.get(url=serpapi_url)

    # Parse the JSON response
    data = response.json()

    # Extract the product results
    product_results = data.get('shopping_results', [])

    # Extract the prices
    prices = [float(product.get('price', '0').replace('$', '').replace(',', '')) for product in product_results]

    # Sort the prices in ascending order
    sorted_prices = sorted(prices)

    # Get the lowest price from the top five results
    lowest_price = sorted_prices[0] if sorted_prices else "No prices found"

    # Update the result label
    result_label.config(text=f"Model Number: {model_number}\n\nLowest Price: ${lowest_price}")

# Create the GUI window
window = tk.Tk()
window.title("Google Shopping Price Checker")

title = tk.Label(window, text="Enter the model number:")
title.pack(padx=10, pady=10)

# Create the model entry widget
model_entry = tk.Entry(window, width=50)
model_entry.pack(padx=10, pady=10)

# Create the check button
check_button = tk.Button(window, text="Check Price", command=get_lowest_price)
check_button.pack(padx=10, pady=10)

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack(padx=10, pady=10)

# Start the GUI loop
window.mainloop()
