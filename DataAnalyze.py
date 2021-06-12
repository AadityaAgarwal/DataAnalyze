import pandas as pd
import plotly_express as px
import plotly.graph_objects as go
import csv

df = pd.read_csv('DataAnalyze.csv')
data = df.groupby(['student_id','level'],as_index=False)['attempt'].mean()
fig = px.scatter(data,
                 x='student_id',
                 y=['level'],
                 color='attempt',
                 size='attempt'
                 )
fig.show()
print(data)
