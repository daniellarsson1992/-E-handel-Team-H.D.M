import matplotlib.pyplot as plt
import pandas as pd

from src.metrics import revenue_by_category

def plot_revenue_by_category(df):
    fig,ax = plt.subplots()
    revenue_by_category(df).plot(kind="bar",ax = ax)
    ax.set_title("Intäkt per kategori")
    ax.set_ylabel("Intäkt i kronor")
    ax.set_xlabel("Kategorier")
    
    return fig,ax



def plot_sales_over_time(df):
    fig,ax = plt.subplots()
    df_copy = df.copy()
    df_copy["date"] = pd.to_datetime(df_copy["date"])
    daily_sales = df_copy.groupby("date")["revenue"].sum()
    daily_sales.plot(ax = ax)
    ax.set_title("Intäkt per dag")
    ax.set_ylabel("Intäkt i kronor")
    ax.set_xlabel("Datum")
    
    
    return fig,ax