from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# ---------- CONFIGURATION ----------
LOGIN_URL = "https://stathead.com/users/login.cgi?redirect_uri=https%3A//stathead.com/fbref/"  # Replace with actual login URL
BASE_URL = "https://stathead.com/fbref/player-match-finder.cgi?request=1&match=player_game&match_status=1&comp_gender=m&comp_type=c-9&timeframe=seasons&year_min=2023-2024&order_by_asc=1&height_type=height_meters&is_qualifier=0&weight_type=kgs&year_max=2023-2024&order_by=date&force_min_year=1&cstat[1]=xg&ccomp[1]=gt&cval[1]=0&cstat[2]=shots&ccomp[2]=gt&cval[2]=0&cstat[3]=passes_completed&ccomp[3]=gt&cval[3]=0&cstat[4]=tackles&ccomp[4]=gt&cval[4]=0&cstat[5]=offsides&ccomp[5]=gt&cval[5]=0&offset={offset}"
BASE_URL = "https://stathead.com/fbref/player-match-finder.cgi?request=1&year_min=2021-2022&comp_gender=m&force_min_year=1&order_by_asc=1&order_by=date&match_status=1&match=player_game&year_max=2021-2022&comp_type=c-9&weight_type=kgs&is_qualifier=0&timeframe=seasons&height_type=height_meters&cstat[1]=xg&ccomp[1]=gt&cval[1]=0&cstat[2]=shots&ccomp[2]=gt&cval[2]=0&cstat[3]=passes_completed&ccomp[3]=gt&cval[3]=0&cstat[4]=tackles&ccomp[4]=gt&cval[4]=0&cstat[5]=offsides&ccomp[5]=gt&cval[5]=0&offset={offset}"
USERNAME = "ScooterKingen"               # Replace with your username
PASSWORD = "L$Bnf8sgyt1921"               # Replace with your password
DRIVER_PATH = r"C:\Users\ASUS\Desktop\chromedriver-win64\chromedriver.exe"
    # Replace with the path to chromedriver

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode (no browser window)
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

# Initialize the WebDriver
service = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)


def login():
    driver.get(LOGIN_URL)
    time.sleep(2)  # Allow page to load

    # Find the username and password fields
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Enter login details and submit
    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)
    password_field.submit()

    time.sleep(5)  # Wait for login to complete

def scrape_page(offset):
    url = BASE_URL.format(offset=offset)
    driver.get(url)
    time.sleep(5)  # Allow page to load

    try:
        table = driver.find_element(By.ID, "stats")
        rows = table.find_elements(By.TAG_NAME, "tr")

        page_data = []
        i = 0
        for row in rows:
            # Skip rows with class 'over_header thead' or 'thead'
            if "over_header thead" in row.get_attribute("class") or "thead" in row.get_attribute("class"):
                continue

            cells = row.find_elements(By.TAG_NAME, "th") + row.find_elements(By.TAG_NAME, "td")
            row_data = [cell.text for cell in cells]
            if row_data and i != 0:
                page_data.append(row_data)
            i+=1

        return page_data

    except Exception as e:
        print(f"No table found for offset {offset}. Stopping.")
        return None

# ---------- MAIN SCRIPT ----------
try:
    login()

    all_data = []
    offset = 0

    while True:
        print(f"Scraping data for offset {offset}...")
        data = scrape_page(offset)
        if not data:
            break
        all_data.extend(data)
        offset += 200

    # Define dynamic columns based on the number of fields
    if all_data:
        num_columns = len(all_data[0])
        columns = [f"Column_{i+1}" for i in range(num_columns)]

        # Create DataFrame and save to CSV
        df = pd.DataFrame(all_data, columns=columns)
        df.to_csv("fbref_scraped_data.csv", index=False)
        print("Data successfully scraped and saved to fbref_scraped_data.csv")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()