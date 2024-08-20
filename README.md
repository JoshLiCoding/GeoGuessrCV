# GeoGuessrCV

[GeoGuessr](https://www.geoguessr.com/) is a popular web-based game that asks you to guess locations from Google Street View images. GeoGuessr professionals memorize many tricks to accurately guess their location.

To dumb things down a bit, can I use CV to differentiate between street views of Paris, Toronto and LA?

## Web Scraping

I used Selenium in Python to screen capture 200-300 images from each city with [Instant Street View](https://www.instantstreetview.com/), which provides Google Street View with location randomization. I manually filtered ~200 images based on quality, and reduced each image's dimension to 256x256.
![alt text](readme-images/webScrape.png)
