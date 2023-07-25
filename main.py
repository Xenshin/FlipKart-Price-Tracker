import requests
from bs4 import BeautifulSoup
import time
import smtplib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime



# Gmail account details for sending email notification
gmail_user = "maryan.tiwari12345@gmail.com"
gmail_password = "xbkpbhnvuajyysmr"


# Log file name and path
log_file = "price_history_log.txt"


# Lists to store price and timestamp data
prices = []
timestamps = []


def log_price(price):
    # Get the current date and time
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    # Open the log file in append mode and write the price and timestamp
    with open(log_file, 'a') as file:
        file.write(f"{current_time} - {price}\n")



def get_user_input():
    # Prompt user to input product URL
    product_url = input("Enter the Flipkart product URL: ")

    # Prompt user to input target price
    while True:
        target_price_input = input("Enter the target price for the product: ")
        try:
            target_price = float(target_price_input)
            break
        except ValueError:
            print("Invalid input! Please enter a valid target price.")

    return product_url, target_price


def update_graph(frame, product_url, target_price):
    cur_price = check_price(product_url)
    log_price(cur_price)
    prices.append(cur_price)
    timestamps.append(datetime.now().strftime('%H:%M:%S'))
    if len(prices) > 30:  # Keep data for the last 30 seconds
        prices.pop(0)
        timestamps.pop(0)
    plt.cla()
    plt.plot(timestamps, prices, marker='o', linestyle='-')
    plt.axhline(y=target_price, color='r', linestyle='--', label='Target Price')
    plt.xlabel('Timestamp')
    plt.ylabel('Price (INR)')
    plt.title('Price History (Last 30 seconds)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    if cur_price <= target_price:
        print(f"It's time to buy the product! The current price is {cur_price}.")
        send_email_notification(target_price)  # Send email notification on price drop

def check_price(product_url):
    # Fetch webpage
    r = requests.get(product_url)
    # Parse the HTML
    soup = BeautifulSoup(r.content, 'html5lib')
    # Extract price using class '_16Jk6d'
    price = soup.find('div', attrs={"class": "_16Jk6d"}).text
    # Remove Rs symbol from price
    price_without_Rs = price[1:]
    # Remove commas from price
    price_without_comma = price_without_Rs.replace(",", "")
    # Convert price from string to float
    float_price = float(price_without_comma)
    return float_price


def send_email_notification(target_price):
    subject = "Price Drop Alert!"
    body = f"The price of the product has dropped to {target_price}. It's time to buy!"
    message = f"Subject: {subject}\n\n{body}"

    try:
        # Establish a secure connection with Gmail's SMTP server
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        # Log in to the Gmail account
        server.login(gmail_user, gmail_password)
        # Send the email notification
        server.sendmail(gmail_user, gmail_user, message)
        # Close the SMTP connection
        server.close()
        print("Email notification sent successfully!")
    except Exception as e:
        print(f"Failed to send email notification: {e}")
        

def track_product_price(product_url, target_price):
    print("Product URL:", product_url)
    print("Target Price:", target_price)


    while True:
        cur_price = check_price(product_url)
        log_price(cur_price)  # Log the current price
        print(f"Current price is {cur_price}")
        if cur_price <= target_price:
            print(f"It's time to buy the product! The current price is {cur_price}.")
            send_email_notification(target_price)  # Send email notification on price drop
            break
        time.sleep(60)


def compare_prices(product_url, other_websites):
    """Compare the price of the product on Flipkart with other websites.

    Args:
        product_url (str): The Flipkart product URL.
        other_websites (dict): A dictionary containing other website URLs and XPath expressions for price extraction.

    Returns:
        dict: A dictionary containing the website names and their respective prices for the product.
    """
    price_comparison = {}

    # Fetch Flipkart price
    flipkart_price = check_price(product_url)
    price_comparison["Flipkart"] = flipkart_price

    # Fetch prices from other websites
    for website, xpath_expression in other_websites.items():
        try:
            r = requests.get(website)
            r.raise_for_status()  # Raise an exception if the request fails

            # Check if the response status code is 503 (Service Unavailable)
            if r.status_code == 503:
                print(f"Failed to fetch price from {website}: Service Unavailable (503 Error)")
                continue

            soup = BeautifulSoup(r.content, 'html.parser')  # Use 'html.parser' instead of 'html5lib'
            price_element = soup.select_one(xpath_expression)
            if price_element:
                price = price_element.text.strip()
                # Assuming the price is in the format "Rs. 123,456" or similar
                price_without_Rs = price.split()[-1].replace(",", "")
                float_price = float(price_without_Rs)
                price_comparison[website] = float_price
            else:
                print(f"Failed to fetch price from {website}: Price element not found.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch price from {website}: {e}")
        except Exception as e:
            print(f"Error while fetching price from {website}: {e}")

    return price_comparison





def main():
    print("Welcome to the Flipkart Product Price Tracker!")
    
    # Get user input for product URL and target price
    product_url, target_price = get_user_input()

    # Ask user for other websites' price comparison
    compare_choice = input("Do you want to compare prices on other websites? (y/n): ").lower()
    if compare_choice == 'y':
        other_websites = {}
        while True:
            website_url = input("Enter the website URL to compare price (or 'done' to finish): ").strip()
            if website_url.lower() == 'done':
                break
            price_tag = input("Enter the HTML tag for the price (e.g., 'div', 'span', etc.): ").strip()
            other_websites[website_url] = price_tag

        if other_websites:
            print("Comparing prices on other websites...")
            price_comparison = compare_prices(product_url, other_websites)
            print("\nPrice Comparison Results:")
            for website, price in price_comparison.items():
                print(f"{website}: {price} INR")

    print("Plotting the price graph (refreshes every 30 seconds)...")

    # Create a figure and use FuncAnimation to continuously update the graph
    plt.figure(figsize=(10, 6))
    ani = FuncAnimation(plt.gcf(), update_graph, fargs=(product_url,target_price), interval=3000)  # 3 seconds in milliseconds
    plt.show()

    

if __name__ == "__main__":
    main()