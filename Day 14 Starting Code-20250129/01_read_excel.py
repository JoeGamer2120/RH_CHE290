"""
This file demonstrates how you can import information from and export
information to Excel.

We are going to get time/temperature data from 3 separate thermocouples that is
stored in an Excel file. We will perform some data processing then create a 
plot. Finally, we will sort the data from each thermocouple and store that
information in a new Excel file. 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    names, data = get_data()
    print(names, data)
    # avg, std, max_data, min_data = get_stats(data)
    # max_time, max_tc = locate_max(data, max_data)
    # min_time, min_tc = locate_min(data, min_data)
    # make_figure(data, avg, std, max_time, max_data, min_time, min_data)
    # write_to_excel(np.sort(data[:, 1:], 0), "Sorted_data.xlsx")
    
def get_data(): 
    """
    This function will read the Excel file and assign the information to
    relevant variable names before return the information.

    Returns
    -------
    names : ndarray
        The names of each column.
    data : ndarray
        The temperature data.

    """
    ###########################################################################
    # IMPORTING DATA FROM EXCEL
    #
    # We can import Excel sheets using: 
    #   pd.read_excel("filename") 
    # from the Pandas library. 
    # 
    # Pandas will import the sheet's information into what's called a DataFrame 
    # (hence, the variable name df). It will automatically put the top row
    # into labels. Thus, we can extract that information into its own variable
    # by using:
    #    variable_name.columns
    #
    # Additionally, working with the numeric information in a DataFrame can be
    # tricky. However, we can easily convert any DataFrame into an array by
    # using:
    #    variable_name.to_numpy()
    #
    # NOTE: if you have a csv file, you can use:
    #        pd.read_csv("filename")    
    ###########################################################################

    ###########################################################################
    # TODO 1: Read the code below, then run the program. Examine the data
    #         that gets printed.
    ###########################################################################

    ###########################################################################
    # TODO 2: You should have noticed that the data printed from TODO 1 is not
    #         the data we are trying to retrieve, because the data was pulled
    #         from the first worksheet in the file. We can get the correct
    #         data by specifying the worksheet that we want to take the data
    #         from.
    #
    #         Uncomment the second read_excel line below (you can comment out
    #         the first, or leave it. It won't make a difference...why?)
    #
    #         After you have verified that we have the correct data, comment
    #         out the 'print' line in main().
    #
    #         You can add print statements below function calls in main() to
    #         verify each function is performing correctly.
    ###########################################################################
    
    
    df = pd.read_excel('Data File.xlsx')
    # df = pd.read_excel('Data File.xlsx', 'Temperature Data')
    names = df.columns.to_numpy()
    data = df.to_numpy()

    return names, data

def get_stats(data):
    """
    This function determines:
        - The average
        - The standard deviation
        - The maximum
        - The minimum
    for all of the temperature data.  

    """
    avg = np.mean(data[:, 1:])
    std = np.std(data[:, 1:])
    max_data = np.max(data[:, 1:])
    min_data = np.min(data[:, 1:])
    
    return avg, std, max_data, min_data

def locate_max(data, my_max):
    """
    This function will find the time where the maximum temperature occurred
    and the thermocouple that measured it.

    Parameters
    ----------
    data : ndarray
        The time/temperature data for each thermocouple
    my_max : float
        The maximum temperature in the data.

    Returns
    -------
    hour : float
        The time where the maximum occurred.
    tc : int
        The number of the thermocouple that read the maximum.

    """
    for i in range(len(data)):
        for j in range(1, len(data[0]+1)):
            if data[i, j] == my_max:
                hour = i
                tc = j    
    return hour, tc

def locate_min(data, my_min):
    """
    This function will find the time where the minimum temperature occurred
    and the thermocouple that measured it.

    Parameters
    ----------
    data : ndarray
        The time/temperature data for each thermocouple
    my_min : float
        The minimum temperature in the data.

    Returns
    -------
    hour : float
        The time where the minimum occurred.
    tc : int
        The number of the thermocouple that read the minimum.

    """
    
    ###########################################################################
    # TODO 3: Complete this function. See locate_max if you need help.
    #
    #         Once you have completed this function, you can uncomment the
    #         call to it in main().
    ###########################################################################
    

def make_figure(data, avg, std, max_time, max_data, min_time, min_data):
    
    ###########################################################################
    # TODO 4: Create a figure of the data. The figure and axes instances have
    #         already been created for you.
    #
    #         Here, instead of line plots, we only want to plot the points
    #         since they are data. To do so, you can use:
    #           ax.scatter(x, y, arguments)
    #
    #         Use the following markers in order (make a list or tuple of str):
    #           triangle (use 2), square, circle
    #
    ###########################################################################

    fig, ax = plt.subplots()

    ###########################################################################
    # TODO 5: Add the following features to the figure:
    #           - The range on x from 0 to 25
    #           - The label on x: time (hour)    
    #           - The label on y: temperature (oF) ...where o is superscripted
    #           - Tick marks in
    ###########################################################################



    ###########################################################################
    # TODO 6: Now add the following LINES to the figure:
    #           - A horizontal black dashed line at the average.
    #           - A horizontal blue dotted line at the average + std    
    #           - A horizontal red dotted line at the average - std
    ###########################################################################
    
    ###########################################################################
    # TODO 7: Finally, we are going to add annotations to the figure. To an
    #         annotation, you use:
    #           ax.annotate("label", xy = (x, y))
    #
    #         In the above, "label" is the message for the annotation and
    #         (x, y) is a tuple of x and y coordinates for the placement of
    #         of the annotation. There are numerous more options to create
    #         more stylized annotations, but we will keep it simple here.
    #
    #         Add two annotations: "max" and "min". Use an x-coordinate of the
    #         time where those values occurred and a y-coordinate equal to 
    #         there values.
    #
    #         The initial placement of those values probably looks a little off
    #         so shift the x value +1.5 and shift the y-value -0.75.
    #
    #         After you have completed all of these TODOs, you can compare your
    #         figure to the included "figure_1.png".
    ###########################################################################    



def write_to_excel(data, filename):
    ###########################################################################
    # WRITING DATA TO EXCEL
    #
    # This function outlines a general scheme for writing data to an Excel
    # file. Because 'data' is an array and not a DataFrame, we first convert
    # the information back into a DataFrame. We then use the two lines of code
    # to write the DataFrame information into the file with filename. We could
    # also add sheet names if desired.
    ###########################################################################
    
    data = pd.DataFrame(data)

    with pd.ExcelWriter(filename) as writer:
        data.to_excel(writer)

main()