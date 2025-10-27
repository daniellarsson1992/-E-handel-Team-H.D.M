import pandas as pd

def total_revenue(df):
    return df['revenue'].sum()

def total_units(df):
    return df['units'].sum()

def aov(df):
    return df['revenue'].sum()/df['units'].sum()

def revenue_by_category(df):
    return df.groupby('category')['revenue'].sum().sort_values(ascending =False)

def top_categories(df, n =3):
    return revenue_by_category(df).head(n)

def revenue_by_city(df):
    return df.groupby('city')['revenue'].sum().sort_values(ascending = False)

def median_revenue(df):
    return df['revenue'].median()

def standard_deviation(df):
    return df['revenue'].std()

def revenue_over_time(df):
    df = df.copy()
    # df = df.dropna(subset=["date"]) # om vi hade haft tomma värden i "date" kolumnen
    # df = df.sort_values("date")
    resultat = df.groupby("date")["revenue"].sum()
    return resultat
