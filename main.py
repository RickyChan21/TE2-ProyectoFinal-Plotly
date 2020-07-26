import pandas as pd
import plotly.express as px

data = pd.read_csv('daily.csv')
data['date'] = pd.to_datetime(data['date'], format = '%Y%m%d').astype(str)
data_cases = data[['date','state','positive']]

fig = px.choropleth(data_cases,                                    # dataframe de los casos
                     locationmode = "USA-states",                  # mapa
                     locations = 'state',                          # division por estados
                     scope = "usa",                                # proyeccion                        
                     color = "positive",                           # columna a graficar (casos positivos)                   
                     hover_name = "state",                         # informacion al hacer hover
                     animation_frame = "date",                     # columna a animar (fechas)
                     color_continuous_scale = 'YlGnBu',            # escala de colores
                     range_color = [0, 500000],                    # rango de los datos a graficar
                     title = "Casos de COVID-19 en Estados Unidos" # titulo
                     )  

fig.show()          
fig.write_html("map.html")