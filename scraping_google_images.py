import time
import os
import requests
import io
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Driver for ChromeDriver
service = ChromeService(ChromeDriverManager().install())
wd = webdriver.Chrome(service=service)


# Get and list images from Google
def get_images_from_google(webd, delay, max_images, url):
    def scroll_down(wdrive):
        wdrive.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(delay)

    url = url
    webd.get(url)

    image_urls = set()
    skips = 0

    while len(image_urls) + skips < max_images:
        scroll_down(webd)
        thumbnails = webd.find_elements(By.CLASS_NAME, 'Q4LuWd')

        for img in thumbnails[len(image_urls) + skips:max_images]:
            try:
                img.click()
                time.sleep(delay)
            except Exception as e:
                print(e)
                continue
            # n3VNCb is to get link to image
            images = webd.find_elements(By.CLASS_NAME, 'n3VNCb')
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
        # get the IO output bytes for the image
        img_file = io.BytesIO(image_content)
        # store file in mem and covert to image file with PIL(pillow package)
        image = Image.open(img_file)
        file_pth = down_path + file_name

        with open(file_pth, 'wb') as file:
            image.save(file, image_type)

        if verbose:
            print(f'TheImage: {file_pth}downloaded successfully')
    except Exception as e:
        print(f'unable to download image from google using driver due to\n:{str(e)}')


async def main(ctx):
    # Google Photos URL
    google_urls = [
        'https://www.google.com/search?q=cortana&tbm=isch&ved=2ahUKEwinieej8IH7AhXewCkDHcIUBlcQ2-cCegQIABAA&oq=cortana'
        '&gs_lcp=CgNpbWcQAzIECCMQJzIECCMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEO'
        'gQIABBDOggIABCxAxCDAToICAAQgAQQsQM6CggAELEDEIMBEEM6BwgAELEDEEM6CwgAEIAEELEDEIMBUPwFWKsOYMgPaABwAHgAgAE5iAGSA'
        '5IBATiYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=Xz5bY-fdEt6Bp8kPwqmYuAU&bih=979&biw=1920&rlz=1C1MSIM_enU'
        'S959US959'
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
    total_number_of_examples = 1
    for url_current, lbl in zip(google_urls, labels):
        urls = get_images_from_google(wd, 0.2, total_number_of_examples, url_current)

        for i, url in enumerate(urls):
            await ctx.send(url)


async def quit_wd():
    wd.quit()  # kil web driver
