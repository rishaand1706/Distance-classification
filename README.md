# Distance-classification
Face Clustering and Classification Report

Introduction

The objective of this study is to cluster facial images based on their hue and saturation value using K-means clustering. It hypothesizes that a detected face will be distributed, while that of a template image is going to be classified based on the generated clusters.

Methodology

The analysis begins with face detection in the input image using OpenCV's Haar Cascade classifier. The detected faces are then converted to the HSV color space, and the hue and saturation values extracted. These serve as feature vectors for clustering with K-means with two clusters.

Cluster centroids are computed, and the detected faces are visualized in a scatter plot according to their hue and saturation values. A template image follows similar processing, and its cluster membership is predicted by the trained K-means model.

Results

Faces have been detected and clustered successfully in two groups. The centroids represent the dominant hue and saturation values of the grouped faces. The template image was analyzed and its hue-saturation features placed it in one of the two clusters.

Conclusion

The clustering approach successfully clustered facial images according to color properties allowing clear distinction between the two clusters. This methodology can be extended for analysis and classification purposes on other facial data sets or different domains where color-based clustering can play an important role.
