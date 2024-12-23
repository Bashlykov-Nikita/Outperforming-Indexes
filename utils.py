import sys

sys.dont_write_bytecode = True
import calc as c
import pandas as pd

# * File with supportive functions


def resample_data(index_data: pd.DataFrame) -> pd.DataFrame:
    """
    Resamples the input index data to monthly frequency by compounding the returns and converting the data to monthly periods.
    """
    index_data = index_data.to_timestamp()
    index_data_m = index_data.resample("M").apply(c.compound).to_period("M")
    return index_data_m


def add_none_to_list(l: list) -> list:
    """Adds "None" string to the beginning of a list.
        This function is used to add "None" options to select bars
    Args:
        l (list): list of options.

    Returns:
        list: list of options which begins with "None".
    """
    return ["None"] + l


def table_highlight(df: pd.DataFrame) -> pd.DataFrame:
    """
    Highlight specific cells in a DataFrame for visual emphasis.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to highlight.

    Returns:
    - pd.DataFrame: The DataFrame with highlighted cells.
    """
    return (
        df.style.applymap(lambda _: "background-color: #262730", subset=(df.index[-1],))
        .highlight_max(
            axis=0,
            props="background-color:#09ab3b;",
            subset=["Return", "Sharpe Ratio", "Max Drawdown"],
        )
        .highlight_min(
            axis=0,
            props="background-color:#ff2b2b;",
            subset=["Return", "Sharpe Ratio", "Max Drawdown"],
        )
        .highlight_max(
            axis=0,
            props="background-color:#ff2b2b;",
            subset=["Volatility", "VaR (5%)", "CVaR (5%)"],
        )
        .highlight_min(
            axis=0,
            props="background-color:#09ab3b;",
            subset=["Volatility", "VaR (5%)", "CVaR (5%)"],
        )
    )
