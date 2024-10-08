from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
import time

# Single out 1 city at a time to run for consistent scraping results
# Use below alternatives to fetch more images in case of poor image quality, update code accordingly
# Paris alternative: https://www.instantstreetview.com/@48.850354,2.324601,284.53h,5p,1z,CAoSLEFGMVFpcE5HclpUNWN5OS1UTVh4ZGxlRDZtanJYaExpekMyV0tndF9kUnRo
# Toronto alternative: https://www.instantstreetview.com/@43.659784,-79.382745,-81.03h,5p,1z,offNuI0FRzrYox3PjtmeiQ
cities = {
    'Paris': 'https://www.instantstreetview.com/@48.85686,2.350793,6.28h,5p,0.54z,OhfFvJtQtsX99vDPqX_Z9A',
    'Toronto': 'https://www.instantstreetview.com/@43.648709,-79.385452,171.97h,5p,1z,t88MR7X7O8sc9G8Rv3ToWg',
    'LosAngeles': 'https://www.instantstreetview.com/@34.031592,-118.458344,-177.54h,5p,1z,yBxxXQHee0158_dmDbj_CQ',
}

driver = webdriver.Chrome()
for city, url in cities.items():
    driver.get(url)
    closeMapButton = driver.find_element(By.ID, 'maparrow')
    closeMapButton.click()

    for i in range(200):
        randomizeButton = driver.find_element(By.ID, 'random-button')
        randomizeButton.click()

        time.sleep(3)
        img = driver.get_screenshot_as_png()
        im = Image.open(BytesIO(img))
        im = im.crop((0, 350, 3000, 1300)) # crop out ads and blank space
        im.save(city + '/' + str(i) + '.png')
driver.quit()