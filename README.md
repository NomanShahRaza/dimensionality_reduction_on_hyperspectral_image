# Dimensionality Reduction Technique on Hyperspectral Image
**The basic intuition of dimensionality reduction techniques is to reduce computation complexity and the size of data.**
## Principal Component Analysis (PCA)
**PCA is a mathematical algorithm that reduces the dimensionality of the data while retaining most of the variation in the data set.**

**Following are the steps to perform PCA:**

*Step 1: Calculate the mean and standard deviation for each feature.*

*Step 2: Calculate the covariance matrix for the whole dataset.*

*Step 3: Compute eigenvalues and eigenvectors of the covariance matrix.*

*Step 4: Sort the eigenvalues and eigenvectors.*

*Step 5: Create an eigenvector matrix with k eigenvalues.*

*Step 6: Transformed the original datasets.*


## Code Explanation

* The hyperspectral image is read using the scipy library. 
* The RGB bands of Hyperspectral Image are displayed using spectral python.
* The PCA is applied on HSI using sklearn.

## Data availability

* The data is publicly available on the below link:

