# Module 9 - Lab 1

Following the example we walked through in class, and another example on Github (https://github.com/summerela/intro_programming_python/blob/master/Module8/4_Analysis_Pipeline.ipynb), create a jupyter notebook that completes the following steps. Upload the notebook to your github repo and submit the link for credit or post your notebook file. 

Use the following data set to answer the questions for your homework

`import pandas as pd`   
`import matplotlib.pyplot as plt`  
  
`# run plots in the notebook`  
`%matplotlib inline`   
`url = "http://pbpython.com/extras/sample-salesv2.csv"`   
`sales = pd.read_csv(url)`  

* Rename the columns to use underscores instead of spaces
* Subset the dataframe to contain only the name, category, quantity and unit price columns
* Subset the dataframe to contain only shirt sales
* Calculate the total cost per shirt sale
* Group the shirt sales by company name
* Pull out top 10 shirt sales
* Graph the top 10 shirt sales
* Save the notebook as either a PDF or HTML page
* Upload it to your github repo
* Post a link to your jupyternote book for credit
