# GeoGuessrCV

[GeoGuessr](https://www.geoguessr.com/) is a popular web-based game that asks you to guess locations from Google Street View images. GeoGuessr professionals memorize many tricks to accurately guess their location.

To dumb things down a bit, can I use CV to differentiate between street views of Paris, Toronto and LA?

## Web Scraping

I used Selenium in Python to screen capture 200-300 images from each city with [Instant Street View](https://www.instantstreetview.com/), which provides Google Street View with location randomization. I manually filtered ~200 images based on quality, and reduced each image's dimension to 256x256.
![Web scrape result](readme-images/webScrape.png)

## HOG + SVM

Histogram of Oriented Gradient (HOG) preprocesses an image by extracting gradients with the Sobel filter, subdividing these gradients into cells, normalizing cells over larger blocks, and finally compiling each cell into a histogram. HOG captures edges well and offers resiliency to geometric and photometric transformations.
![HOG](readme-images/HOG.png)

Support Vector Machine (SVM) performs classification using flattened HOG vectors. Using GridSearchCV (3-fold), I found the rbf kernel and a regularization parameter (C) of 10 to be the best hyperparameter values.

This yields an accuracy of 68.5% and a confusion matrix as follows
![HOG + SVM confusion matrix](readme-images/HOGConfM.png)
