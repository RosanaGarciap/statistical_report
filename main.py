####################################################################
# AUTHOR: ROSANA GARCIA
# CSE 230
# SRINT 2: DATA ANALYSIS 
# Main program for analysing general cases os diseases registered
# in diverse hospitals
####################################################################

#   IMPORT PYTHON LIBRARIES
import pandas as pd
import os
from datetime import date
from datetime import datetime

#   IMPORT CUSTOMIZED SOURCE FUNCTIONS
from searching import *

DISEASES = ["Arthritis", "Asthma", "Cancer", "Diabetes", "Hypertension", "Obesity"]

# LOAD DATAFRAME FROM CSV FILE
cwd = os.getcwd()
filename = "healthcare_dataset.csv"
file_path = os.path.join(cwd, filename)
df = pd.read_csv(file_path) 

# EXTRACTING DATA

# Convert string date instance to datetime instance
df["Date of Admission"] = pd.to_datetime(df['Date of Admission'])


# Select subdataframe from original that contains the data we need to work with 
testing_data = df[["Medical Condition", "Gender", "Hospital", "Date of Admission"]]

# Seting current date and adjust date format to Year/Month/Day

current_date = date.today().strftime("%d/%m/%Y")
starting_date = datetime.strptime("2023/01/01", '%Y/%m/%d')
starting_date_case2 = datetime.strptime("2024/01/01", '%Y/%m/%d')
pdf_title = "Healthcare Data Analysis Report"

#Selecting plotting data 
plots = medical_center_assistence(testing_data, DISEASES, starting_date)

# How much cases of each disease the area have had since 2023?
show_plot(plots, "Diseases quantity report from {} to {}".format(starting_date.strftime("%d/%m/%Y"), current_date))

#How many cases of Female and male patients with Diabetes we have had since 2023? 
all_that(testing_data, DISEASES[3], starting_date, starting_date_case2)
