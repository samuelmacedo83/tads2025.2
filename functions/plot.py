import plotly.express as px
from plotly.graph_objects import Figure
from functions.download import download_data

def plot_ts(ticker:str) -> Figure:
    """
    Plots the closing stock price time series for a given ticker symbol.
    Parameters:
        ticker (str): The stock ticker symbol.
    Returns:
        Figure: A Plotly Figure object representing the time series plot.  
    """
    df = download_data(ticker)

    fig = px.line(
        df,
        x = 'Date', 
        y = 'Close',
        title = f'{ticker} Stock Price'
    )
    
    return fig
