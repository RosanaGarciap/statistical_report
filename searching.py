#######################################################################
# AUTHOR: ROSANA GARCIA
# CSE 230
# Filtering, plotting and file writing functions.
#######################################################################

# Importing libraries
from pypdf import PdfWriter
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# Function Name: all_that
# INPUT: 
#   df: dataset
#   _columname: column name we want to analyse
#   that_condition: single value constrain we want to analize
# OUTPUT:
#   amount: number of cases (rows) that satisfy the given condition

def all_that(df, _columname, that_condition):
    df1 = df.loc[(df[_columname] == that_condition) ]
    amount = df1.value_counts()
    return amount

# Function Name: all_that
# INPUT: 
#   df: dataset
#   _columname: string of columns names we want to analyse
#   that_conditions: array of single values we want to analize
#   from_date: date from which start to analyse
# OUTPUT:
#   amount: number of cases (rows) that satisfy the given condition

def all_that(df, _columname, from_date, to_date = date.today().strftime("%Y/%m/%d") ): 
    plottings = []

    general_result = df.loc[(df["Medical Condition"] == _columname)  & ( df["Date of Admission"] >= from_date) & ( df["Date of Admission"] <= to_date) ]
    female_result = general_result.loc[(df["Gender"] == "Female")]
    male_result = general_result.loc[(df["Gender"] == "Male")]

    female_general_result = female_result.groupby('Date of Admission', as_index=False).agg('count')
    male_general_result = male_result.groupby('Date of Admission', as_index=False).agg('count')
    
    plottings.append(female_general_result[["Date of Admission", "Gender"]])
    plottings.append(male_general_result[["Date of Admission", "Gender"]])
    
    show_spectroscopy(plottings)
 
# Function Name: medical_center_assistence 
# INPUT: 
#   df: dataset
#   _columnames: array of columns names we want to analyse
#   that_conditions: array of single values we want to analize
#   from_date: date from which start to analyse
# OUTPUT:
#   amount: number of cases (rows) that satisfy the given condition
#
# DESCRIPTION: Returns all the cases attended for every disease from
# a given date until current date

def medical_center_assistence(df, diseases, from_date):
    plottings = {}
    #print(hospital_centers.iloc[0])

    for disease in diseases:
         
        #print(disease)
        result = df.loc[(df["Medical Condition"] == disease) & ( df["Date of Admission"] >= from_date)]
        if not result.empty:
            row_number = result["Medical Condition"].count()
            if row_number > 2:
                #print (row_number)
                plottings[disease] = row_number
    return plottings

# Function Name: show_plot
# INPUT: 
#   plot: array of dataset
#   title: string containing the title of the image
# OUTPUT:
#   None
# DESCRIPTION: if not exist, this programe creates a 
# pdf file that contains all the ploting made

def show_plot(plots, title):

    with PdfPages('barplot_.pdf') as pdf:
        header_values = list(plots.keys())
        #print(header_values)
        height_values = list(plots.values())
        axe_y = [250, 500, 550, 600, 650, 700]
        print(height_values)

        plt.figure()
        plt.bar(header_values, height_values)

        # plot's title
        plt.title(title)

        # X and Y labels
        plt.xlabel("Medical Condition")
        plt.ylabel("Number of Admission Cases")

        for i in range(0, len(header_values)):
            plt.text(header_values[i], height_values[i], str(height_values[i]), ha="center" )

        # visualizing the plot
        #plt.show()

        #Saving plot unto pdf file
        pdf.savefig()

        #close object
        plt.close()

# Function Name: show_spectrocopy
# INPUT: 
#   plot: array of dataset
# OUTPUT:
#   None
# DESCRIPTION: if not exist, this programe creates a 
# pdf file that contains all the ploting made
def show_spectroscopy(scattered_plots):
    with PdfPages('timespan_analysis_plot.pdf') as pdf:
        y_values = list( scattered_plots[0]["Gender"])
        x_values = list( scattered_plots[0]["Date of Admission"])
        y2_values = list( scattered_plots[1]["Gender"])
        x2_values = list( scattered_plots[1]["Date of Admission"])

        fig, ax = plt.subplots(1)
        fig.set_size_inches(14,6)

        #print("###########################################")
        #get columns names for labels
        ax.plot(x_values, y_values, label="Female")           
        ax.plot(x2_values, y2_values,label="Male")   
        ax.legend()        
        ax.grid(True)
        pdf.savefig()
        
    plt.close()
