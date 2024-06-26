# Importing the necessary libraries
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.common.keys import Keys

# Initialize a Chrome WebDriver
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the target webpage
browser.get("https://mrbeast.store/")
time.sleep(5)

# Click on the cookie consent button
browser.find_element(By.XPATH, '/html/body/section[1]/div/div[2]/button[3]').click()
time.sleep(5)
browser.find_element(By.XPATH, '/html/body/div[21]/dialog/div/div[2]/div/button[2]').click()

# Function to scrape name of item
def get_name(item):
    name_tag = item.find('h3', class_='card__heading')
    if name_tag and name_tag.a:
        full_name = name_tag.a.text.strip()
        # Splitting the name and removing the color part, assuming it's separated by " - "
        name_parts = full_name.split(" - ")
        if len(name_parts) > 1:
            return " - ".join(name_parts[:-1]).strip()
        return full_name
    return None

# Function to scrape colour of item
def get_colour(soup):
    alt_text = soup.find('img', {'class': 'motion-reduce'})['alt']
    if alt_text:
        parts = alt_text.split(" - ")
        if len(parts) > 1:
            return parts[-1].strip()
    return None

# Function to scrape price of item
def get_price(soup):
    price_tag = soup.find('span', class_='price-item--regular')
    if price_tag:
        return price_tag.text.strip()
    return None

# Function to scrape store site
def scrape():
    # Parse HTML Code With Beautiful Soup and Selenium
    time.sleep(2)
    body = browser.find_element(By.TAG_NAME, 'body')
    for _ in range(40):  # Adjust the range as needed
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    soup = BeautifulSoup(browser.page_source, features='html.parser')

    # Find all elements with a class attribute
    all_elements = soup.find_all(True, class_=True)
    time.sleep(2)
    main_page = soup.find('div', id="Infinite-Loop")
    # Parsing Items
    # Get all elements with the 'product-grid' id using Selenium
    items = main_page.find_all('li', class_='grid__item')
    name = []
    colour = []
    price = []

    for item in items:
        name.append(get_name(item))
        colour.append(get_colour(item))
        price.append(get_price(item))
    df = pd.DataFrame({"Name": name, "Colour": colour, "Price": price})
    return df

# Function to get new data
def get_new_data():
    global new_df  # Use the global variable
    browser.find_element(By.XPATH, '/html/body/div[9]/sticky-header/header/nav/ul/li[1]/a/span').click()
    new_df = scrape()
    browser.back()
    time.sleep(2)

# Function to get BeastActive data
def get_BeastActive_data():
    global BA_df
    browser.find_element(By.XPATH, '/html/body/div[9]/sticky-header/header/nav/ul/li[2]/a/span').click()
    time.sleep(5)
    BA_df = scrape()
    browser.back()
    time.sleep(2)

# Function to get BeastOrignal data
def get_BeastOrignal_data():
    global BO_df
    browser.find_element(By.XPATH, '/html/body/div[9]/sticky-header/header/nav/ul/li[3]/a/span').click()
    time.sleep(2)
    BO_df = scrape()
    browser.back()
    time.sleep(2)

# Function to get Tops data
def get_Tops_data():
    global tops_df
    browser.find_element(By.XPATH, '/html/body/div[9]/sticky-header/header/nav/ul/li[4]/a/span').click()
    time.sleep(2)
    tops_df = scrape()
    browser.back()
    time.sleep(2)

# Function to get Bottoms data
def get_Bottoms_data():
    global bottoms_df
    browser.find_element(By.XPATH, '/html/body/div[9]/sticky-header/header/nav/ul/li[5]/a/span').click()
    time.sleep(2)
    bottoms_df = scrape()
    browser.back()
    time.sleep(2)

# Function to get Kids data
def get_Kids_data():
    global kids_df
    browser.find_element(By.XPATH, '/html/body/div[9]/sticky-header/header/nav/ul/li[6]/a/span').click()
    time.sleep(2)
    kids_df = scrape()
    browser.back()
    time.sleep(2)

# Function to get Accessories data
def get_Accessories_data():
    global acc_df
    browser.find_element(By.XPATH, '/html/body/div[9]/sticky-header/header/nav/ul/li[7]/a/span').click()
    time.sleep(2)
    acc_df = scrape()
    browser.back()
    time.sleep(2)

# Function to get user input
def get_user_input():
    options = ['New', 'BeastActive', 'BeastOrignal', 'Tops', 'Bottoms', 'Kids', 'Accessories']

    print("Select an option:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            user_input = int(input("Enter the number corresponding to your choice: "))
            if 1 <= user_input <= len(options):
                return options[user_input - 1]
            else:
                print("Invalid number. Please enter a number between 1 and", len(options))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to start the program
def start():
    while True:
        selected_option = get_user_input()

        if selected_option in selected_options_set:
            print(f"You have already selected {selected_option}. Please choose a different option.")
            continue

        selected_options_set.add(selected_option)

        if selected_option == 'New':
            get_new_data()
        elif selected_option == 'BeastActive':
            get_BeastActive_data()
        elif selected_option == 'BeastOrignal':
            get_BeastOrignal_data()
        elif selected_option == 'Tops':
            get_Tops_data()
        elif selected_option == 'Bottoms':
            get_Bottoms_data()
        elif selected_option == 'Kids':
            get_Kids_data()
        elif selected_option == 'Accessories':
            get_Accessories_data()
        else:
            print("Invalid option. Exiting.")
            break

        print("You selected:", selected_option)
        user_input = input("Do you want to continue? (y/n): ").lower()
        if user_input != 'y':
            print("Exiting.")
            break

# Initialize DataFrames
new_df = pd.DataFrame()
BA_df = pd.DataFrame()
BO_df = pd.DataFrame()
tops_df = pd.DataFrame()
bottoms_df = pd.DataFrame()
kids_df = pd.DataFrame()
acc_df = pd.DataFrame()

# Initialize selected options set
selected_options_set = set()

# Call the start function
start()



dataframes = [('BeastActive', BA_df), ('BeastOrignal', BO_df), ('tops', tops_df), ('bottoms', bottoms_df), ('kids', kids_df), ('accessories', acc_df)]

# Iterate over each DataFrame
for df_name, df in dataframes:
    # Check if the DataFrame is not empty
    if not df.empty:
        # Merge new_df with the current DataFrame
        merged_df = pd.merge(new_df, df, on=['Name', 'Colour', 'Price'], how='inner')

        # Check if there are common items
        if not merged_df.empty:
            # Display or save the common items
            print(f"Common items in new_df and {df_name} DataFrame:")
            print(merged_df)

            # Save the common items to a CSV file
            merged_df.to_csv(f'common_items_{df_name}.csv', index=False)
        else:
            print(f"No common items found in new_df and {df_name} DataFrame")
    else:
        print(f"{df_name} DataFrame is empty, skipping.")

#Export DataFrames to CSV if not empty
if not new_df.empty:
    new_df.to_csv('new_data.csv', index=False)

if not BA_df.empty:
    BA_df.to_csv('BeastActive_data.csv', index=False)

if not BO_df.empty:
    BO_df.to_csv('BeastOrignal_data.csv', index=False)

if not tops_df.empty:
    tops_df.to_csv('tops_data.csv', index=False)

if not bottoms_df.empty:
    bottoms_df.to_csv('bottoms_data.csv', index=False)

if not kids_df.empty:
    kids_df.to_csv('kids_data.csv', index=False)

if not acc_df.empty:
    acc_df.to_csv('accessories_data.csv', index=False)

# Close the browser
browser.close()