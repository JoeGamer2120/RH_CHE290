"""
We will use this file to walk through how to use the debugger to find errors
in our code.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    years, data, months = unpack_data()
    # avgs = get_averages(data)
    # plot_avgs(years, avgs)
    
def unpack_data():
    """
    This function will read in the data from the Lake Powell sheet in the
    Excel file, then place the information into the three returned variables.

    Returns
    -------
    years : ndarray
        The years for which there are data.
    months : ndarray
        The list of months.
    data : ndarray
        The monthly data for each year in a table.

    """

    df = pd.read_excel('Data File.xlsx', 'Lake Powell')
    years = df.columns.to_numpy()
    data = df.to_numpy()
    months = data[0]
    
    return years, months, data

def yearly_avg(data_for_year):
    """
    This function takes a single vector of data for a provided year and 
    determines the average level for that year.

    Parameters
    ----------
    data_for_year : ndarray
        The monthly level data for a provided year.

    Returns
    -------
    float
        The average level for the provided year.

    """
    total = 0
    
    for i in range(len(data_for_year)):
        total += data_for_year[i]
    
    return total/12


def get_averages(data):
    """
    This function creates a vector of yearly level averages. It uses the 
    yearly_avg function to calculate the average for each year individually.

    Parameters
    ----------
    data : ndarray
        The monthly levels for each year in tabular form.

    Returns
    -------
    avgs : ndarray
        A vector of average levels for each year.

    """

    avgs = np.zeros(12)

    for i in range(len(data)):
        avgs[i] = yearly_avg(data[i])
    
    return avgs

def plot_avgs(years, avgs):
    """
    Complete this function to create a plot of the average level vs year.
    Your plot should have the following features:
        - A dashed, blue line of linewidth 2.
        - Circles for markers of the data.
        - Tick marks in.
        - x-axis label of "Year"
        - y-axis label of "Average Level"

    Parameters
    ----------
    years : ndarray
        A vector of the years.
    avgs : ndarray
        A vector of the average levels for each year.

    Returns
    -------
    None.

    """


main()