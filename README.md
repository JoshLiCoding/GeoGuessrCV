# GeoGuessrCV

[GeoGuessr](https://www.geoguessr.com/) is a popular web-based game that asks you to guess locations from Google Street View images. GeoGuessr professionals memorize many tricks to accurately guess their location.

I'm not as good as GeoGuessr professionals, so can I use CV to differentiate between street views of Paris, Toronto and LA? Here, I experimented with 3 models: HOG + SVM, a custom CNN and a pretrained ResNet.

## Web Scraping

I used Selenium in Python to screen capture 200-300 images from each city with [Instant Street View](https://www.instantstreetview.com/), which provides Google Street View with location randomization. I manually filtered ~200 images based on quality, and reduced each image's dimension to 256x256.

<img src="readme-images/webScrape.png" width=800>

Some sample images:

<img src="readme-images/sampleImages.png" width=800>

## 1. HOG + SVM

_SKLearn, SKImage_, _MatPlotLib_

Histogram of Oriented Gradient (HOG) is an image processing technique that 1) extracts gradients with Sobel filters, 2) subdivides these gradients into cells, 3) normalizes cells over larger blocks, and 4) compiles each cell into a histogram. HOG captures edges well and offers resiliency to geometric and photometric transformations. Below are some sample HOG transformations on my dataset:

<img src="readme-images/HOG.png" width=300>

Next, a Support Vector Machine (SVM) performs multi-class prediction using flattened HOG vectors. With GridSearchCV, I found the rbf kernel and a regularization parameter (C) of 10 to be the best hyperparameter values. This yields an accuracy of **68%** and a confusion matrix as follows:

<img src="readme-images/HOGConfM.png" width=400>

Clearly, the model has the hardest time deciding between Toronto and Paris. This makes sense with the style of buildings we see!

## 2. Custom CNN

_PyTorch_

A Convolutional Neural Network (CNN) is a neural network that learns via filter optimization. Here, I built a custom 3-layer CNN using the following architecture (activations are batch normalized and reLU activated, although not shown):

<img src="readme-images/CNNArch.png" width=700>

The CNN is trained with mini-batch GD for 10 epochs. With relatively arbitrary architecture choice and hyperparameter initialization, the above model consistently performs with **~70% accuracy** on testing data. We can plot a sample learning curve below:

<img src="readme-images/CNNCurve.png" width=400>

Let's also visualize the performance of the model (with parameters from the best-performing epoch) using a confusion matrix:

<img src="readme-images/CNNConfM.png" width=400>

We can see that, surprisingly, it tends to predict street views of Paris as LA.

Finally, we can take a look at the weights of every convolution layer. Sometimes, this reveals insights into the exact patterns the model is trying to capture; in our case, it just shows the many diverse filters we are employing.

<img src="readme-images/CNNWeights.png" width=800>

## 3. Transfer Learning w/ ResNet

_PyTorch_

A Residual Neural Network (ResNet) connects traditional CNN layers with skip connections to better train deep models. The ResNet34 architecture is presented below:

<img src="readme-images/ResNetArch.png" width=700>

_credit: https://www.researchgate.net/figure/Architecture-of-ResNet34-29_fig2_368590488_

For this dataset, I loaded a pretrained ResNet34 model and and modified its fully connected layer to output 3 predictions. Since I am not retraining weights of the original ResNet34 model (which essentially acts as a feature extractor), this is known as transfer learning. After 10 epochs, we obtain **~75% accuracy** on testing data. A sample learning curve looks like:

<img src="readme-images/ResNetCurve.png" width=400>

Similar to the CNN model, we can plot the confusion matrix:

<img src="readme-images/ResNetConfM.png" width=400>

This model seems to confuse LA with Toronto instead. Nevertheless, the pretrained ResNet performed the best overall!

### Credits

Much of this work is inspired by what I learned from IBM's Introduction to Computer Vision and Image Processing course.
