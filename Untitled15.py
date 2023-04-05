#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv
import requests
from bs4 import BeautifulSoup

# Send a GET request to the Amazon page
url = 'https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product cards on the page
product_cards = soup.find_all('div', {'data-component-type': 's-search-result'})

# Initialize an empty list to store the data
data = []

# Loop through each product card and extract the required information
for card in product_cards:
    # Extract product name
    try:
        product_name = card.h2.a.span.text.strip()
    except AttributeError:
        product_name = ''
    
    # Extract product price
    try:
        product_price = card.find('span', {'class': 'a-price-whole'}).text.strip()
    except AttributeError:
        product_price = ''
    
    # Extract product rating
    try:
        product_rating = card.find('span', {'class': 'a-icon-alt'}).text.strip().split()[0]
    except AttributeError:
        product_rating = ''
    
    # Extract seller name
    try:
        seller_name = card.find('div', {'class': 'sg-col-16-of-20'}).find('div', {'class': 'a-row a-size-base a-color-secondary'}).span.text.strip()
    except AttributeError:
        seller_name = ''
    
    # Append the extracted data to the list
    if product_name and product_price and product_rating:
        data.append([product_name, product_price, product_rating, seller_name])

# Write the data to a CSV file
with open('amazon_products.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Price', 'Rating', 'Seller Name'])
    writer.writerows(data)


# In[ ]:




