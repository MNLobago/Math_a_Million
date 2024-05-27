# Basic Statistical Analysis Script

This script performs basic statistical analysis on a given CSV file. It provides various statistics, visualizations, and hypothesis tests for each column in the dataset.

## Features

- Computes basic statistics (mean, median, mode, variance, standard deviation) for numerical columns.
- Computes the mode and frequency distribution for categorical columns.
- Generates histograms and box plots for numerical columns.
- Generates bar plots for categorical columns.
- Performs t-tests for numerical columns.
- Performs chi-square tests for categorical columns.

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scipy

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/Basic_stats.git
   cd Basic_stats

Install the required packages:

You can install the required packages using pip:

`pip install pandas numpy matplotlib seaborn scipy`

Usage
Prepare Your CSV File:

Ensure your CSV file is accessible and contains the data you want to analyze. Note the file path.

Run the Script:

Execute the script in your terminal:

`python3 basic_stats.py`

When prompted, enter the path to your CSV file:

`Enter the path to your CSV file: /path/to/your/csvfile.csv`

Interpret the Output:

The script will display basic statistics, create visualizations, and perform hypothesis tests for each column in the CSV file.

Script Functionality
Loading Data:
The script loads data from a specified CSV file using pandas.

Basic Statistics for Numerical Columns:
Mean: Average value.
Median: Middle value.
Mode: Most frequent value.
Variance: Measure of data dispersion.
Standard Deviation: Measure of data spread.
Basic Statistics for Categorical Columns:
Mode: Most frequent category.
Frequency Distribution: Count of each category.
Visualizations:
Histogram: Distribution of numerical data.
Box Plot: Summary of numerical data distribution.
Bar Plot: Frequency distribution of categorical data.
Hypothesis Tests:
T-Test for Numerical Columns: Compares the column mean to a population mean.
Chi-Square Test for Categorical Columns: Tests the independence of categorical variables.
Example Output:


Basic Statistics for trans:
  Mode: Automatic (S8)
  Frequency: {'Automatic (S8)': 814, 'Automatic (S6)': 739, ...}
  
Basic Statistics for cylinders:
  Mean: 5.468
  Median: 5.0
  Mode: 4
  Variance: 3.527
  Std_dev: 1.878

  T-Test (population mean = 0):
    T-statistic: 116.847, P-value: 0.000

Error Handling:
The script includes basic error handling for:

File not found errors.
Incorrect data types.
Missing values.




