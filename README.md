# Overview

<!-- {Important!  Do not say in this section that this is college assignment.  Talk about what you are trying to accomplish as a software engineer to further your learning.} -->
This software was developed to enhance skills with analyzing data programmatically. The goal with this project is to practice utilizing the functions from the Python Pandas library.

<!-- {Provide a description of the data set that you are analyzing.  Include the link of where you obtained the data.} -->
The data being analyzed is a breakdown of nutritional facts collected regarding several menu items from different fast food restaurants, such as McDonalds, Subway, or Chick-Fil-A.
Dataset for Fast Food Nutrition Information found on [Kaggle](https://www.kaggle.com/datasets/ulrikthygepedersen/fastfood-nutrition?resource=download).

<!-- {Describe your purpose for writing this software to analyze the data.} -->
There are two main files to consider with this project- one being a jupyter notebook that walks through each of the questions and demonstrates the use of the pandas library. The other being the 'fastfood.py' file which when run the user can enter in data to dynamically create tables similar to those answered in the questions. The program then opens the html file it creates in a web browser for the user to view.

<!-- {Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the data set, the questions and answers, the code running and a walkthrough of the code.} -->

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

<!-- {List the questions and the answers you found by doing this analysis.} -->
* **Question 1:** Is Chick-Fil-A healthier than McDonalds with regards to calories? 

See [Jupyter Notebook Question 1](summary.ipynb)

* **Question 2:** What items contain the highest amount of sodium? What about protein?

See [Jupyter Notebook Question 2](summary.ipynb)

* **Question 3:** What are the nutritional facts across a related group of foods such as burgers/sandwiches/nuggets?

See [Jupyter Notebook Question 3](summary.ipynb)

# Development Environment

<!-- {Describe the tools that you used to develop the software}
{Describe the programming language that you used and any libraries.} -->


# Useful Websites

<!-- {Make a list of websites that you found helpful in this project} -->
* [Pandas Overview](https://pandas.pydata.org/docs/getting_started/overview.html)
* [Python Docs](https://docs.python.org/3/library/csv.html)
* [Pandas 10 Minute Tutorial](https://pandas.pydata.org/docs/user_guide/10min.html#min)

# Future Work

<!-- {Make a list of things that you need to fix, improve, and add in the future.} -->
* Improve display
    * The html that is displayed currently is not as clean as I would like. In the future I want the tables to look similar to how they would appear for the jupyter notebook and get that more professional look either in a web browser or with a gui.
* Improve interface
    * While researching the styling for the tables in the pandas documentation it mostly discussed using this for exporting either LaTex or html. I would like to learn how to use these stylized tables in a python gui and have interactive buttons for dynamically creating the tables rather than having to enter in the data via a terminal.