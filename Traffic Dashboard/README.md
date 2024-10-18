# Bangalore Traffic Dashboard

This project is a traffic monitoring dashboard for Bangalore city, built using [Dash](https://dash.plotly.com/) and Plotly. It visualizes key traffic metrics, such as traffic volume, average speed, congestion levels, and incident reports. Users can filter data by date range, area, road/intersection, weather conditions, and roadwork activities.

## Features

- **Date Range Filtering**: Select a date range to analyze traffic data over a specific period.
- **Area and Road/Intersection Selection**: Choose specific areas and roads/intersections to narrow down the analysis.
- **Weather Condition and Roadwork Filtering**: Filter traffic data based on weather conditions and roadwork activities.
- **Traffic Volume and Average Speed**: Visualize traffic volume and average speed over time using line charts.
- **Congestion Level Heatmap**: View congestion levels using a heatmap that shows average congestion by date and hour.
- **Incident Reports Pie Chart**: Analyze the distribution of traffic incidents with a pie chart.

## Prerequisites

- Python 3.x
- The following Python libraries:
  - `dash`
  - `pandas`
  - `numpy`
  - `plotly`

Install dependencies via `pip`:
```bash
pip install dash pandas numpy plotly
