# flipkart-price-tracker
## Description

The Flipkart Product Price Tracker is a Python application that allows users to track the price of a product listed on Flipkart and receive email notifications when the product's price drops below a specified target price. The application fetches the product's current price from Flipkart and logs the price along with timestamps in a text file for historical price tracking. It also provides the option to compare the product's price on Flipkart with other websites.

The tracker includes the following key features:

- Real-time Price Tracking: The application continuously monitors the product's price on Flipkart and updates the price graph every 3 seconds, displaying the last 30 seconds of price history.
- Historical Price Logging: The application logs the product's price along with timestamps in a text file, allowing users to track the price history over time.
- Price Drop Notification: When the product's price falls below the user-defined target price, the application sends an email notification, alerting the user that it's time to buy the product at a discounted price.

## Documentation

### Prerequisites

1. Python 3.x installed on the system.
2. Required Python libraries: requests, BeautifulSoup, matplotlib.

### Usage

1. Run the `flipkart_price_tracker.py` script using Python.
2. Enter the Flipkart product URL and target price when prompted.
3. Optionally, choose to compare the product's price on other websites by providing their URLs and HTML tags.
4. The real-time price graph and historical price plot will be displayed, and the application will continuously update the price graph every 3 seconds.

### Features

1. **Real-time Price Tracking:** The application fetches the product's current price from Flipkart and updates the price graph every 3 seconds to show the latest 30 seconds of price history.
2. **Historical Price Logging:** The application logs the product's price along with timestamps in a text file named `price_history_log.txt`. This file stores the historical price data for future reference.
3. **Price Drop Notification:** When the product's price falls below the user-defined target price, the application sends an email notification to the specified Gmail account. The email serves as an alert to the user that the product is available at a discounted price.
4. **Website Price Comparison:** Users can choose to compare the product's price on Flipkart with other websites by providing the URLs and HTML tags of those websites. The application fetches the prices from the specified websites and displays them for comparison.

# First Draft

> ********************Where the URL is already entered and the target price is already entered.********************
> 

```python
PYTHON SCRIPT:

import requests
from bs4 import BeautifulSoup
import time
product_url = "https://www.flipkart.com/logitech-g502-hero-25k-sensor-adj-dpi-upto-\
    25600-rgb-11-programmable-buttons-wired-optical-gaming-mouse/p/itma269dc20e3570?\
    pid=ACCFUJC6N8ZCHESF&lid=LSTACCFUJC6N8ZCHESFGMWWLO&marketplace=FLIPKART&store\
    =6bo%2Fai3%2F2ay&srno=b_1_8&otracker=hp_rich_navigation_3_1.navigationCard\
    .RICH_NAVIGATION_Electronics~Gaming~Gaming%2BMouse_DZSR0ADA14Y0&otracker1\
    =hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_\
    navigationCard_cc_3_L2_view-all&fm=organic&iid=en_TdMRumvU-\
    YgauISYMbQqGnNp0-IHhil-lkMHDAnQr4Dq4IxfBauid4756rSIlBc9y3rLqybyb\
    _Nbodq9rZhYow%3D%3D&ppt=browse&ppn=browse&ssid=jgbnhbt5400000001690255835758"

# setting the target price
target_price = 3000
def check_price():
    # fetch webpage
    r = requests.get(product_url)
    # parse the html
    soup = BeautifulSoup(r.content, 'html5lib')
    # extract price using class '_16Jk6d'
    price = soup.find('div', attrs={"class": "_16Jk6d"}).text
    # remove Rs symbol from price
    price_without_Rs = price[1:]
    # remove commas from price
    price_without_comma = price_without_Rs.replace(",", "")
    # convert price from string to int
    int_price = int(price_without_comma)
    return int_price
cur_price = check_price()
print(f"Current price is {cur_price}")
print("We will inform you, once price of product hits out target price")
print("Waiting...")
while True:
    # get current price
    cur_price = check_price()
    if cur_price <= target_price:
        print(f"Its time to buy product, its current price is {cur_price}")
        break
    # wait for 1 minute to check again
    time.sleep(60)
```

---

---

# Second Draft

> ********************User input for product URL and target price********************
> 

The "User Input for Product URL and Target Price" feature enhances the existing Python script to allow users to input the product URL and set their desired target price for tracking. This empowers users to track various products with different target prices without modifying the script's code each time.

```python
import requests
from bs4 import BeautifulSoup
import time
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
def track_product_price(product_url, target_price):
    print("Product URL:", product_url)
    print("Target Price:", target_price)
    while True:
        # Get current price
        cur_price = check_price(product_url)
        print(f"Current price is {cur_price}")
        if cur_price <= target_price:
            print(f"It's time to buy the product! Current price is {cur_price}")
            break
        # Wait for 1 minute to check again
        time.sleep(60)
def main():
    print("Welcome to the Flipkart Product Price Tracker!")
    
    # Get user input for product URL and target price
    product_url, target_price = get_user_input()
    # Start tracking the product price
    track_product_price(product_url, target_price)
if __name__ == "__main__":
    main()

```

![1 ) welcome](https://github.com/Xenshin/flipkart-price-tracker/assets/96466881/ffb52148-76e6-40e9-9cde-3063852a022f)



![2](https://github.com/Xenshin/flipkart-price-tracker/assets/96466881/5fb85095-9416-4e3f-8917-665ed553ec30)


### **ENTER THE TARGET PRICE:**

![3) enter the target price](https://github.com/Xenshin/flipkart-price-tracker/assets/96466881/05c5af4b-6ee1-4c9b-9784-ccfc13891f16)


### **FINAL OUTPUT**

![4) final output](https://github.com/Xenshin/flipkart-price-tracker/assets/96466881/2c1b9fd4-74a3-432b-a967-00535bde208a)


---

---

# Third Draft

> ****Email Notification Feature Documentation****
> 

The Email Notification feature is an enhancement to the existing Python script that tracks the price of a product on Flipkart. With this feature, users can receive email notifications when the product's price drops below their specified target price. The email notification ensures that users stay informed about potential price reductions and can take advantage of purchasing the product at a discounted rate.

```python
import requests
from bs4 import BeautifulSoup
import time
import smtplib

# Gmail account details for sending email notification
gmail_user = "something@example.com"
gmail_password = "xxxx-xxxx-xxxx-xxxx"

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
    while True:
        cur_price = check_price(product_url)
        print(f"Current price is {cur_price}")
        if cur_price <= target_price:
            print(f"It's time to buy the product! The current price is {cur_price}.")
            send_email_notification(target_price)  # Send email notification on price drop
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
```

![5) email sent](https://github.com/Xenshin/flipkart-price-tracker/assets/96466881/69ccb757-e093-49b3-80a8-7185ba0bd6dc)


![6) mail ss](https://github.com/Xenshin/flipkart-price-tracker/assets/96466881/bb58a42b-98c6-479d-bd2e-c9753a8bfb95)


# Fourth Draft

> **************************************************Logging Price History Feature**************************************************
> 

The "Logging Price History" feature is an enhancement to the existing Python script designed to track the price of a product on Flipkart. This feature allows users to keep a record of the product's price over time. The price history is saved in a log file, enabling users to analyze past price trends and make informed purchasing decisions.

```python
import requests
from bs4 import BeautifulSoup
import time
import smtplib

# Gmail account details for sending email notification
gmail_user = "something@example.com"
gmail_password = "xxxx-xxxx-xxxx-xxxx"

# Log file name and path
log_file = "price_history_log.txt"

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
def main():
    print("Welcome to the Flipkart Product Price Tracker!")
    
    # Get user input for product URL and target price
    product_url, target_price = get_user_input()
    # Start tracking the product price
    track_product_price(product_url, target_price)
if __name__ == "__main__":
    main()
```

![7) log file ss](https://github.com/Xenshin/flipkart-price-tracker/assets/96466881/c0c91bd8-d56f-4b87-b980-f2d1d4376a43)


# Fifth Draft

> **************************************************Price Graph Feature**************************************************
> 

The "Price Graphs" feature is an enhancement to the existing Python script designed to track the price of a product on Flipkart. This feature allows users to visualize the price history of the product over time by creating graphical representations (line charts) of the price data. Users can easily interpret the price trends and fluctuations using these graphs.

```python
import requests
from bs4 import BeautifulSoup
import time
import smtplib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

# Gmail account details for sending email notification
gmail_user = "something@example.com"
gmail_password = "xxxx-xxxx-xxxx-xxxx"

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
def main():
    print("Welcome to the Flipkart Product Price Tracker!")
    
    # Get user input for product URL and target price
    product_url, target_price = get_user_input()
    print("Plotting the price graph (refreshes every 30 seconds)...")
    # Create a figure and use FuncAnimation to continuously update the graph
    plt.figure(figsize=(10, 6))
    ani = FuncAnimation(plt.gcf(), update_graph, fargs=(product_url,target_price), interval=30000, save_count=None)  # 30 seconds in milliseconds
    plt.show()
if __name__ == "__main__":
    main()
```

![8) price history plot](https://github.com/Xenshin/flipkart-price-tracker/assets/96466881/0613483b-ad6b-4ebb-98d8-3766e943f0b1)

