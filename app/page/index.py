# -*- coding: utf-8 -*-
"""Application index.

This is the first page users will see when they visit your app.
"""
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Your Value Proposition

            Emphasize how the app will benefit users. Don't emphasize the underlying technology.

            ✅ mydashapp is a running app that adapts to your fitness levels and designs personalized workouts to help you 
            improve your running. 

            ❌ mydashapp is the only intelligent running app that uses sophisticated deep neural net machine learning to 
            make your run smarter because we believe in ML driven workouts. 

            """
        ),
        dcc.Link(
            dbc.Button("Your Call To Action", color="primary"), href="/predictions"
        ),
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(
    gapminder.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

column2 = dbc.Col([dcc.Graph(figure=fig),])

layout = dbc.Row([column1, column2])
