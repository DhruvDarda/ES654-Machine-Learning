''' In this file, you will utilize two parameters degree and include_bias.
    Reference https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class PolynomialFeatures():
    
    def __init__(self, degree=2,include_bias=True):
        """
        Inputs:
        param degree : (int) max degree of polynomial features
        param include_bias : (boolean) specifies wheter to include bias term in returned feature array.
        """
        self.degree = degree
        self.include_bias = include_bias
    
    def transform(self,X_t):
        """
        Transform data to polynomial features
        Generate a new feature matrix consisting of all polynomial combinations of the features with degree less than or equal to the specified degree. 
        For example, if an input sample is  np.array([a, b]), the degree-2 polynomial features with "include_bias=True" are [1, a, b, a^2, ab, b^2].
        
        Inputs:
        param X : (np.array) Dataset to be transformed
        
        Outputs:
        returns (np.array) Tranformed dataset.
        """
        final = []
        for i in range(len(X_t)):
            X = np.array(X_t[i]).reshape(1,-1)
            if self.include_bias:
                X = np.insert(X, 0, 1, axis=0)
            X = X.reshape(-1, 1)
            X_i = X.T
            for i in range(1, self.degree):
                X_i = np.matmul(X, X_i).reshape(1, -1) #.reshape(X.shape[0], X_i.shape[1])
                X_i = np.unique(X_i, axis=1).reshape(1, -1)
            final.append(X_i.flatten())
        return np.array(final)