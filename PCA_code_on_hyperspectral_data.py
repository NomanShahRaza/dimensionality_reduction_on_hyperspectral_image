# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 11:19:44 2021

@author: noman
"""
#%%##################### Import Libraries #################%%#

from spectral import *
import scipy.io
from sklearn.decomposition import PCA

#%%############## Read Hyperspectral Dataset ##############%%#

mat = scipy.io.loadmat(r"D:\Hyperspectral_dataset_Pavia\Cuprite.mat")
mat.keys()
data3d=mat['X']
row,column,bands=mat['X'].shape

#%% Display the RGB image of HSI

imshow(data3d, (16, 100, 180))

#%%######################### Apply PCA ####################%%#


new_data3d= data3d.reshape((data3d.shape[0]*data3d.shape[1]), data3d.shape[2])
pca = PCA(n_components = 100)
PCs = pca.fit_transform(new_data3d)

reduced_data3d=PCs.reshape(row,column,PCs.shape[1])
imshow(reduced_data3d)
