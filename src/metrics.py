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

