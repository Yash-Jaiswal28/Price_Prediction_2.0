from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Abstract Base Class for Bivariate Analysis Strategy

# This class defines a common interface for bivariate analysis strategies.
# Subclasses must implement the analyze method

class BivariateAnalysisTemplate(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Perform bivariate analysis on two features of the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature1 (str): The name of the first feature/column.
        feature2 (str): The name of the second feature/column.

        Returns:
        None: This method visualize the relationship between the two features.
        """
        pass

# Concrete Strategy for Numerical vs Numerical Analysis

# This strategy analyzes the relationship between two numerical features using scatter plots
class NumericalVsNumericalAnalysis(BivariateAnalysisTemplate):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Plots the relationship between two numerical features using a scatter plot.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature1 (str): The name of the first numerical feature/column to be analyzed.
        feature2 (str): The name of the second numerical feature/column to be analyzed.

        Returns:
        None: Displays a scatter plot showing the relationship between the two features.
        """
        plt.figure(figsize=(10,6))
        sns.scatterplot(data=df, x=feature1, y=feature2)
        plt.title(f"{feature1} VS {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()