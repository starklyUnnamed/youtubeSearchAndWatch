import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def main():  # sourcery skip: extract-duplicate-method, extract-method
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
        """try:
            playButton = browser.find_element(By.XPATH, "//button[@title='Play (k)']")
        except NoSuchElementException: 
            playButton = browser.find_element(By.XPATH, "//div[@id='columns']")
        playButton.click()"""
    skip_ads(browser)

def skip_ads(browser):
    skipped = False
    while not skipped:
        try:
            sleep(6)
            skipButton = browser.find_element(By.XPATH, "//button[@class='ytp-ad-skip-button ytp-button']")
            skipButton.click()
        except NoSuchElementException:
            skipped == True
main()