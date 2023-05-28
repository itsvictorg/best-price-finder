# Product Price Checker

The Product Price Checker is a Python application that allows users to search for product prices from popular online retailers. It uses web scraping techniques to retrieve product information and prices from Google Shopping and displays the lowest price from the top results.

## Features

- Search for product prices by entering the model number.
- Retrieves product information and prices from Google Shopping.
- Displays the lowest price found from the top results.
- Filters the search to specific retailers: Walmart, Best Buy, Target, Amazon, B&H, and Andromeda.
- Excludes products with prices less than or equal to zero.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Required Python packages (specified in the `requirements.txt` file)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/product-price-checker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd product-price-checker
   ```

3. Install the required Python packages:

   ```bash
   pip3 install tkinter
   pip3 install requests
   ```

## Usage

1. Run the application by executing the following command:

   ```bash
   python price_checker.py
   ```

2. Enter the model number of the product you want to search for when prompted.

3. The application will retrieve the product information and prices from Google Shopping.

4. The lowest price found from the top results will be displayed, along with the retailer name.

## Customization

- You can modify the list of retailers in the `RETAILERS` constant in the `price_checker.py` file to include or exclude specific retailers.

- The application currently searches the first 8 results on Google Shopping. To change the number of results, modify the `NUM_RESULTS` constant in the `price_checker.py` file.

## Limitations

- The application relies on web scraping techniques and may be subject to changes in the website structure or search results layout of Google Shopping. If any issues arise, please ensure you have the latest version of the application.

- The availability and accuracy of prices may vary depending on the region and product listings on Google Shopping.

## Contributing

Contributions to the Product Price Checker application are welcome! If you encounter any issues, have suggestions, or want to contribute new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

```

Feel free to modify the content according to your specific application and requirements.
