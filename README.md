# GeoGuessrCV

[GeoGuessr](https://www.geoguessr.com/) is a popular web-based game that asks you to guess locations from Google Street View images. GeoGuessr professionals memorize many tricks to accurately guess their location.

To dumb things down a bit, can I use CV to differentiate between street views of Paris, Toronto and LA?

## Web Scraping

I used Selenium in Python to screen capture 200-300 images from each city with [Instant Street View](https://www.instantstreetview.com/), which provides Google Street View with location randomization. I manually filtered ~200 images based on quality, and reduced each image's dimension to 256x256.

<img src="readme-images/webScrape.png" width=800>

## HOG + SVM

Histogram of Oriented Gradient (HOG) is an image processing technique that 1) extracts gradients with Sobel filters, 2) subdivides these gradients into cells, 3) normalizes cells over larger blocks, and 4) compiles each cell into a histogram. HOG captures edges well and offers resiliency to geometric and photometric transformations. Below are some sample HOG transformations:

<img src="readme-images/HOG.png" width=300>

Next, a Support Vector Machine (SVM) performs multi-class prediction using flattened HOG vectors. With GridSearchCV, I found the rbf kernel and a regularization parameter (C) of 10 to be the best hyperparameter values. This yields an accuracy of **68.5%** and a confusion matrix as follows:

<img src="readme-images/HOGConfM.png" width=300>

Clearly, the model has the hardest time deciding between Toronto and Paris. This makes sense with the style of buildings we see!
