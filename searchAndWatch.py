import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def main():
    search = input("What would you like to search youtube for? ").lower()
    watch = input("Would you like to watch the first video? ").lower()
    watch = watch in {"yes", "y", "yeah", "sure", "yup"}
    browser = webdriver.Firefox()
    browser.get(f'https://www.youtube.com/results?search_query={search}')
    if watch:
        sleep(1)
        firstVideo = browser.find_element(By.XPATH, "//yt-formatted-string[@class='style-scope ytd-video-renderer']")
        firstVideo.click()
        sleep(1)
    skip_ads(browser)

def skip_ads(browser):
    skipped = False
    while not skipped:
        try:
            sleep(6)
            skipButton = browser.find_element(By.XPATH, "//button[@class='ytp-ad-skip-button-modern ytp-button']")
            skipButton.click()
        except NoSuchElementException:
            skipped = True
main()