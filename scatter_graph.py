import streamlit as st
import datetime as dt
import pandas as pd
import plotly.express as px


# def create_scatter_plot(data_frame):
#     """
#         Create a scatter plot to visualize the total amount by month and gender.
#
#         Args:
#             data_frame (pd.DataFrame): The DataFrame containing the data.
#
#         Returns:
#             plotly.graph_objects.Figure: The scatter plot.
#         """
#     # Convert order_date to datetime
#     data_frame['order_date'] = pd.to_datetime(data_frame['order_date'])
#
#     # Extract the month from order_date column
#     data_frame['month'] = data_frame['order_date'].dt.month
#
#     # Group by month and gender, and calculate the total amount
#     grouped_df = data_frame.groupby(['month', 'gender', 'full_name'])['total'].sum().reset_index()
#     print(grouped_df)
#     # Define color mapping for male and female
#     color_mapping = {'male': 'blue', 'female': 'red'}
#
#     # Create the scatter plot
#     fig = px.scatter(grouped_df, x='month', y='total', color='gender', color_discrete_map=color_mapping,
#                      labels={ 'month': 'Month', 'total': 'Total'}, title='Total Amount By Month')
#
#     # Set the x-axis range based on the min and max month values
#     fig.update_layout(xaxis_range=[grouped_df['month'].min() - 1, grouped_df['month'].max() + 1])
#
#     # Return the chart
#     return fig


def create_scatter_plot(data_frame):
    """
        Create a scatter plot to visualize the total amount by month and gender.

        Args:
            data_frame (pd.DataFrame): The DataFrame containing the data.

        Returns:
            plotly.graph_objects.Figure: The scatter plot.
        """
    # Convert order_date to datetime
    data_frame['order_date'] = pd.to_datetime(data_frame['order_date'])

    # Extract the month from order_date column
    data_frame['month'] = data_frame['order_date'].dt.month

    # Group by month and gender, and calculate the total amount
    grouped_df = data_frame.groupby(['month', 'gender'])['amount'].sum().reset_index()

    # Define color mapping for male and female
    color_mapping = {'male': 'blue', 'female': 'red'}

    # Create the scatter plot
    fig = px.scatter(grouped_df, x='month', y='amount', color='gender', color_discrete_map=color_mapping,
                     labels={'month': 'Month', 'amount': 'Amount Per Transaction'}, title='Total Amount By Month')

    # Set the x-axis range based on the min and max month values
    fig.update_layout(xaxis_range=[grouped_df['month'].min() - 1, grouped_df['month'].max() + 1])

    # Return the chart
    return fig