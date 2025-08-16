# Obligatory assignment 3

# Task 2

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException, TimeoutException

def extracting_and_printing_links():
    op = Options()
    op.add_argument("--headless")
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=op)
    try:
        driver.get("https://sites.google.com/view/nikt2024?usp=sharing")
        loading = WebDriverWait(driver, 10)
        loading.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href]")))

        pages = set()
        all_links = driver.find_elements(By.CSS_SELECTOR, "a[href]")
        for link in all_links:
            href = link.get_attribute("href")
            if href.startswith("https://sites.google.com/view/") and href not in pages:
                pages.add(href)
        
        for page in pages:
            driver.get(page)
            loading_2 = WebDriverWait(driver, 10)
            loading_2.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='C9DxTc ']")))

            web_element_text = driver.find_elements(By.XPATH, "//span[@class='C9DxTc ']")
            print(f"WEBSITE: {page}")
            for elem in web_element_text:
                print(elem.text)

    except TimeoutException as e:
        print(f"TimeoutException (e.g too much time has passed for this task) gave an error here {page}: {e}")
    except WebDriverException as e:
        print(f"WebDriver gave an error here {page}: {e}")
    except Exception as e:
        print(f"The general catch-all exception gave an error here {page}: {e}")
    finally:
        driver.quit()

extracting_and_printing_links()