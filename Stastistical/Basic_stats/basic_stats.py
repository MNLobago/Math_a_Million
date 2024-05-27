import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

def load_data(file_path):
    return pd.read_csv(file_path)

def basic_stats_numeric(data, column):
    mean = data[column].mean()
    median = data[column].median()
    mode = data[column].mode()[0]
    variance = data[column].var()
    std_dev = data[column].std()
    return mean, median, mode, variance, std_dev

def basic_stats_categorical(data, column):
    mode = data[column].mode()[0]
    frequency = data[column].value_counts().to_dict()
    return mode, frequency

def plot_histogram(data, column):
    plt.figure(figsize=(10, 5))
    sns.histplot(data[column].dropna(), kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_boxplot(data, column):
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=data[column].dropna())
    plt.title(f'Box plot of {column}')
    plt.xlabel(column)
    plt.show()

def plot_barplot(data, column):
    plt.figure(figsize=(10, 5))
    sns.countplot(y=column, data=data, order = data[column].value_counts().index)
    plt.title(f'Bar plot of {column}')
    plt.xlabel('Frequency')
    plt.ylabel(column)
    plt.show()

def perform_ttest(data, column, population_mean):
    t_stat, p_val = stats.ttest_1samp(data[column].dropna(), population_mean)
    return t_stat, p_val

def perform_chisquare(data, column):
    freq = data[column].value_counts()
    chi2_stat, p_val = stats.chisquare(freq)
    return chi2_stat, p_val

if __name__ == "__main__":
    file_path = input("Enter the path to your CSV file: ").strip()
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
    else:
        try:
            data = load_data(file_path)
            population_mean = 0  # Modify as needed for t-test comparison
            
            for column in data.columns:
                print(f"Basic Statistics for {column}:")
                if pd.api.types.is_numeric_dtype(data[column]):
                    mean, median, mode, variance, std_dev = basic_stats_numeric(data, column)
                    print(f"  Mean: {mean}")
                    print(f"  Median: {median}")
                    print(f"  Mode: {mode}")
                    print(f"  Variance: {variance}")
                    print(f"  Std_dev: {std_dev}")
                    
                    plot_histogram(data, column)
                    plot_boxplot(data, column)
                    
                    t_stat, p_val = perform_ttest(data, column, population_mean)
                    print(f"  T-Test (population mean = {population_mean}):")
                    print(f"    T-statistic: {t_stat}, P-value: {p_val}")
                else:
                    mode, frequency = basic_stats_categorical(data, column)
                    print(f"  Mode: {mode}")
                    print(f"  Frequency: {frequency}")
                    
                    plot_barplot(data, column)
                    
                    chi2_stat, p_val = perform_chisquare(data, column)
                    print(f"  Chi-Square Test:")
                    print(f"    Chi-square statistic: {chi2_stat}, P-value: {p_val}")
                    
                print("\n")
        except Exception as e:
            print(f"An error occurred: {e}")
