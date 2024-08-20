# GeoGuessrCV

[GeoGuessr](https://www.geoguessr.com/) is a popular web-based game that asks you to guess locations from Google Street View images. GeoGuessr professionals memorize many tricks to accurately guess their location.

[![Every Trick a Pro GeoGuessr Player Uses to Win (ft. RAINBOLT) | WIRED](https://img.youtube.com/vi/0p5Eb4OSZCs/0.jpg)](https://www.youtube.com/watch?v=0p5Eb4OSZCs)

To dumb things down a bit, can I use CV to differentiate between Paris, Toronto and LA?

## Web Scraping

I used Selenium in Python to screen capture 200-300 images from each city with [Instant Street View](https://www.instantstreetview.com/), which provides Google Street View with location randomization. I manually filtered ~200 images based on quality, and reduced each image's dimension to 256x256.
![alt text](readme-images/webScrape.png)
