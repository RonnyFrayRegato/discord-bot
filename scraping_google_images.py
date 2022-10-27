from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time
import os
import discord
from discord import app_commands

# Driver for ChromeDriver
# service = ChromeService(ChromeDriverManager().install())
# wd = webdriver.Chrome(service=service)
PATH = r'C:\Users\andre\network-project\discord-bot\Chrome Driver\chromedriver.exe'
wd = webdriver.Chrome(executable_path=PATH)


# Get and list images from Google
def get_images_from_google(wd, delay, max_images, url):
    def scroll_down(wd):
        wd.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(delay)

    url = url
    wd.get(url)

    image_urls = set()
    skips = 0

    while len(image_urls) + skips < max_images:
        scroll_down(wd)
        thumbnails = wd.find_elements(By.CLASS_NAME, 'Q4LuWd')

        for img in thumbnails[len(image_urls) + skips:max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue
            # n3VNCb is to get link to image
            images = wd.find_elements(By.CLASS_NAME, 'n3VNCb')
            for image in images:
                if image.get_attribute('src') in image_urls:
                    max_images += 1
                    skips += 1
                    break
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))

    return image_urls


def download_image(down_path, url, file_name, image_type='png', verbose=True):
    try:
        # get image
        image_content = requests.get(url).content
        # get the IO output bytes fo the image
        img_file = io.BytesIO(image_content)
        # store file in mem and covert to image file with PIL(pillow package)
        image = Image.open(img_file)
        file_pth = down_path + file_name

        with open(file_pth, 'wb') as file:
            image.save(file, image_type)

        if verbose == True:
            print(f'TheImage: {file_pth}downloaded successfully')
    except Exception as e:
        print(f'unable to download image from google using driver due to\n:{str(e)}')


async def main(phrase):
    print(phrase)
    # Google Photos URL
    google_urls = [
        'https://www.google.com/search?q=image&hl=EN&tbm=isch&sxsrf=ALiCzsZP3mx80Mnco6UIEPc30uuVJk85eA%3A1666795946831&source=hp&biw=1536&bih=841&ei=qklZY7uDMI-HwbkPiNecoAY&iflsig=AJiK0e8AAAAAY1lXupzXjhc4ETuXivWognraRhHmNkiF&ved=0ahUKEwi7gMnikv76AhWPQzABHYgrB2QQ4dUDCAc&uact=5&oq=image&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQM6BAgjECc6CAgAELEDEIMBUABYlQlghg9oAHAAeACAAX6IAdkCkgEDNC4xmAEAoAEBqgELZ3dzLXdpei1pbWc&sclient=img'
    ]

    # label for my item
    labels = ['Ronny']

    # check the length of labels match our url
    if len(google_urls) != len(labels):
        raise ValueError('The length of Urls doesnt match Labels')

    item_path = 'images/Ronny/'
    # make directory if it doesn't exist
    for lbl in labels:
        if not os.path.exists(item_path + lbl):
            print(f'Making directory:{str(lbl)}')
            os.makedirs(item_path + lbl)

    # loop through the Google urls and labels lists and get the images
    TOTAL_NUMBER_OF_EXAMPLES = 1
    for url_current, lbl in zip(google_urls, labels):
        urls = get_images_from_google(wd, 0.2, TOTAL_NUMBER_OF_EXAMPLES, url_current)

        for i, url in enumerate(urls):
            url = url
            return url
            # await interaction.phrase.send(url)
            # await interaction.url.send(url)

            """download_image(down_path=f'images/Ronny/{lbl}/',
                           url=url,
                           file_name=str(i + 1) + '.png',
                           verbose=True)"""


async def quit_wd():
    wd.quit()  # kil web driver
