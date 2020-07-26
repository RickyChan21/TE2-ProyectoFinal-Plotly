import pandas as pd
import plotly.express as px

data = pd.read_csv('daily.csv')
data_cases = data[['date','state','positive']]

fig = px.choropleth(data_cases,
                     locationmode="USA-states",
                     locations = 'state',
                     scope="usa",                            
                     color="positive",                     # identify representing column
                     hover_name= "state",
                     animation_frame = "date",              # identify hover name        # identify date column        # select projection
                     color_continuous_scale = 'YlGnBu',  # select prefer color scale
                     range_color=[0,500000]              # select range of dataset
                     )        
fig.show()          
fig.write_html("map.html")