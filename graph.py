import pandas as pd
import plotly.express as px

dataFrame = pd.read_csv("corona data.csv")

graph = px.scatter( dataFrame , x = "Date", y = "Cases", color = "Country" )

graph.show()