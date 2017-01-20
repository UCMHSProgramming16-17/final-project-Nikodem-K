# I will be making two graphs on crime in the US
# import pandas and name it "pd" to be able to use the necessary functions
import pandas as pd

# import the desired chart types, output file, and the save function using bokeh
from bokeh.charts import Bar, output_file, save, Scatter

# assign a variable to your data
data = pd.read_csv("crime.csv")

# create the first graph
p = Bar(data, "Year", values = "Population", title="Population in the US Over 18 Years")

# create a file to put the graph into
output_file("year_vs_population")

# save the graph as an html file
save(p)