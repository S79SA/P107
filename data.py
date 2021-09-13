import pandas as pd
import csv 
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

print(df.groupby("level")["student"].mean())

fig = go.Figure(go.Bar(
    x = df.groupby("level")["student"].mean(),
    y = ['Level 1','Level 2','Level 3','Level 4'],
    orientation = 'h'))

fig.show()