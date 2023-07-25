import requests
from bs4 import BeautifulSoup
import time
import smtplib
import matplotlib.pyplot as plt
from datetime import datetime



# Gmail account details for sending email notification
gmail_user = "maryan.tiwari12345@gmail.com"
gmail_password = "xbkpbhnvuajyysmr"


# Log file name and path
log_file = "price_history_log.txt"


def log_price(price):
    # Get the current date and time
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    # Open the log file in append mode and write the price and timestamp
    with open(log_file, 'a') as file:
        file.write(f"{current_time} - {price}\n")


def plot_graph(prices, timestamps):
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, prices, marker='o', linestyle='-')
    plt.xlabel('Timestamp')
    plt.ylabel('Price (INR)')
    plt.title('Price History')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('price_history_graph.png')
    plt.show()



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

    prices = []
    timestamps = []

    while True:
        cur_price = check_price(product_url)
        log_price(cur_price)  # Log the current price
        prices.append(cur_price)
        timestamps.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print(f"Current price is {cur_price}")
        if cur_price <= target_price:
            print(f"It's time to buy the product! The current price is {cur_price}.")
            send_email_notification(target_price)  # Send email notification on price drop
            plot_graph(prices, timestamps)  # Plot the price history graph
            break
        time.sleep(60)

def main():
    print("Welcome to the Flipkart Product Price Tracker!")
    
    # Get user input for product URL and target price
    product_url, target_price = get_user_input()

    # Start tracking the product price
    track_product_price(product_url, target_price)

if __name__ == "__main__":
    main()
