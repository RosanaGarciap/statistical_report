# Overview
Data Analysis comprehends different data processes required to obtain information, these processes include reading, organizing, and analyzing large amounts of data, looking for patterns, trends, and statistical relevance between datasets. For this project, we want to show how to use basic commands of Python libraries for statistical projects and data analysis work, such as Panda, Matplotplib, and data writing with PyPDF2, and explain little details to consider while processing the data we are working with.

Focusing on how Data Analysis can be applied to obtain relevant information in the healthcare field, we selected [healthcare_dataset.csv](https://www.kaggle.com/code/muhammadfurqan0/unlocking-healthcare-trends-data-analysis/input) dataset, available in Kaggle website.

The purpose of this little project is to explain how Python libraries for Statistical analysis can provide functions for plotting, searching, and displaying statistical results.

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

**Question 1:** *What Medical Condition (disease) had more cases since 2023 ?* 
This process requires the sum of all cases registered for each medical condition on the list. to ensure the date span filters and data manipulation are required. The answer to this question can be applied to hospital pharmacies to understand how much medicine for the different treatments is required to have in store to ensure the treatment of the patients.

![Barplot of number of medical diseases from 2023 to 2025](/image/Plot_Image.png)

**Question 2:** *How many Female and male patients with Diabetes required medical treatment between 2023 and 2024?* 
The information gained from processing the dataset provided knowledge regarding whether the cases of one gender have been increasing respect for the other. In this particular case, male and female cases have had consistent distribution, which implicated there was not a tendency to receive more cases of women or men during 2023. To gain more information we could also study the number of cases by year and determine if there has been an increasing number of cases from las decade.
![Plot of Diabetes cases from 2023 to 2025](/image/Spectral_Plot_Image.png)

# Development Environment

Programming Language: Python 3.13.0
Editor: Visual Studio Code 1.97.0
## Libreries

- pypdf2 24.2
- matplotlib
- pandas
- os
- DateTime

## Websites Resources:
* [Real Python](https://realpython.com/creating-modifying-pdf/)

* [Matplotlib](https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html)

* [Multiple plotting](https://matplotlib.org/stable/gallery/lines_bars_and_markers/csd_demo.html#sphx-glr-gallery-lines-bars-and-markers-csd-demo-py)

# Future Work
As you can notice version 1.1 provides functions for specific questions for specific columns to analyze. future version will update functions show_plot() to be able to work receiving more than two columns. searching methods will also be modified to work with searching combinations that work with big volumes of data. 
