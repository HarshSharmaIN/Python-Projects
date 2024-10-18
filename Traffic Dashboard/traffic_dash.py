import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# Initialize the Dash app
app = dash.Dash(__name__)

# Load and preprocess data
df = pd.read_csv('Banglore_traffic_Dataset.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract Hour from the Date column
df['Hour'] = df['Date'].dt.hour

# You don't need this line; it's causing the error:
# dates = np.array(df['Date'].dt.to_pydatetime())

# Define the app layout
app.layout = html.Div([
    html.H1("Bangalore Traffic Dashboard"),
    
    # Date Picker Range for filtering
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date=df['Date'].min().date(),
        end_date=df['Date'].max().date(),
        display_format='YYYY-MM-DD'
    ),
    
    # Dropdowns for area and road/intersection selection
    dcc.Dropdown(
        id='area-dropdown',
        options=[{'label': area, 'value': area} for area in df['Area Name'].unique()],
        value=df['Area Name'].unique()[0]  # Default value
    ),
    
    dcc.Dropdown(
        id='road-dropdown',
        options=[{'label': road, 'value': road} for road in df['Road/Intersection Name'].unique()],
        value=df['Road/Intersection Name'].unique()[0]  # Default value
    ),

    # Additional filters for weather and roadwork
    dcc.Dropdown(
        id='weather-dropdown',
        options=[{'label': condition, 'value': condition} for condition in df['Weather Conditions'].unique()],
        placeholder="Select Weather Condition"
    ),

    dcc.Dropdown(
        id='roadwork-dropdown',
        options=[{'label': activity, 'value': activity} for activity in df['Roadwork and Construction Activity'].unique()],
        placeholder="Select Roadwork Activity"
    ),

    # Graphs for Traffic Volume, Average Speed, Heatmap, and Incident Reports
    dcc.Graph(id='traffic-volume-chart'),
    dcc.Graph(id='average-speed-chart'),
    dcc.Graph(id='traffic-heatmap'),
    dcc.Graph(id='incident-pie-chart')
])

# Define callback to update graphs based on user input
@app.callback(
    [Output('traffic-volume-chart', 'figure'),
     Output('average-speed-chart', 'figure'),
     Output('traffic-heatmap', 'figure'),
     Output('incident-pie-chart', 'figure')],
    [Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date'),
     Input('area-dropdown', 'value'),
     Input('road-dropdown', 'value'),
     Input('weather-dropdown', 'value'),
     Input('roadwork-dropdown', 'value')]
)
def update_charts(start_date, end_date, selected_area, selected_road, selected_weather, selected_roadwork):
    # Convert start_date and end_date to datetime
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter data based on inputs
    filtered_df = df[
        (df['Date'] >= start_date) &
        (df['Date'] <= end_date) &
        (df['Area Name'] == selected_area) &
        (df['Road/Intersection Name'] == selected_road)
    ]
    
    # Apply additional filters
    if selected_weather:
        filtered_df = filtered_df[filtered_df['Weather Conditions'] == selected_weather]
    if selected_roadwork:
        filtered_df = filtered_df[filtered_df['Roadwork and Construction Activity'] == selected_roadwork]

    # If the filtered dataframe is empty, return empty figures
    if filtered_df.empty:
        empty_fig = px.line(title='No Data Available')
        return empty_fig, empty_fig, empty_fig, empty_fig

    # Traffic Volume Over Time
    fig_volume = px.line(filtered_df, x='Date', y='Traffic Volume', title='Traffic Volume Over Time')

    # Average Speed Over Time
    fig_speed = px.line(filtered_df, x='Date', y='Average Speed', title='Average Speed Over Time')

    # Heatmap for Congestion Level
    heatmap_data = filtered_df.groupby(['Date', 'Hour'])['Congestion Level'].mean().reset_index()
    fig_heatmap = px.density_heatmap(heatmap_data, x='Date', y='Hour', z='Congestion Level', title='Congestion Level Heatmap')

    # Pie chart for Incident Reports
    pie_chart_data = filtered_df['Incident Reports'].value_counts().reset_index()
    pie_chart_data.columns = ['Incident Reports', 'Count']
    fig_pie = px.pie(pie_chart_data, values='Count', names='Incident Reports', title='Incident Reports Distribution')

    return fig_volume, fig_speed, fig_heatmap, fig_pie

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
