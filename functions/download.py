import pandas as pd
import yfinance as yf

def download_data(
    ticker:str = 'TSLA'
) -> pd.DataFrame:
    """
    Download historical stock data using yfinance.

    Parameters
    ----------
    ticker : str, optional
        Stock ticker symbol (default is 'TSLA').

    Returns
    -------
    pd.DataFrame
        DataFrame containing historical stock data with columns:
        Date, Open, High, Low, Close, Adj Close, Volume.
    """
    df = yf.download(
        ticker,
        period='max',
        multi_level_index= False
    ).reset_index()

    return df

