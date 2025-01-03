import time
from selenium.webdriver.common.by import By

def add_hashtags(driver, hashtags):
    """Add hashtags to the video description"""
    if not hashtags:
        return

    hashtag_button = driver.find_element(By.CSS_SELECTOR, '[data-e2e="hashtag-selector"]')
    hashtag_button.click()

    for hashtag in hashtags:
        hashtag_input = driver.find_element(By.CSS_SELECTOR, '[data-e2e="hashtag-input"]')
        hashtag_input.send_keys(hashtag)
        
        # Her hashtag'den sonra 1 saniye bekle
        time.sleep(1)
        
        # İlk önerilen hashtag'i seç
        first_hashtag = driver.find_element(By.CSS_SELECTOR, '[data-e2e="hashtag-suggestion-item"]')
        first_hashtag.click() 