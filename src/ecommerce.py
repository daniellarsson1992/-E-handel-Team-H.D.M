from dataclasses import dataclass, field
from .metrics import top_categories, total_revenue, total_units, aov, revenue_by_category, revenue_by_city, median_revenue, standard_deviation
from .viz import plot_sales_over_time, plot_revenue_by_category
import pandas as pd

@dataclass
class Analyzer:
    df: pd.DataFrame
    metrics: dict = field(default_factory=dict)
    plots: dict = field(default_factory=dict)

    def compute_all_calculations(self):
        self.metrics["total_revenue"] = total_revenue(self.df)
        self.metrics["total_units"] = total_units(self.df)
        self.metrics['aov'] = aov(self.df)
        self.metrics['revenue_by_category'] = revenue_by_category(self.df)
        self.metrics['revenue_by_city'] = revenue_by_city(self.df)
        self.metrics['top3_categories'] = top_categories(self.df, n=3)
        self.metrics['median_revenue'] = median_revenue(self.df)
        self.metrics['standard_deviation'] = standard_deviation(self.df)


    def make_the_plots(self):
        self.plots["revenue_by_category"] = plot_revenue_by_category(self.df)
        self.plots["sales_over_time"] = plot_sales_over_time(self.df)

    def summary(self):
        return (
            f"Total Revenue: {self.metrics.get('total_revenue'):.0f}\n"
            f"Total Units Sold: {self.metrics.get('total_units'):.0f}\n"
            f"Average Order Value (AOV): {self.metrics.get('aov'):.0f}\n"
            f"\nTop 3 Categories by Revenue:\n"
            f"{self.metrics.get('top3_categories')}\n"
            f"\nRevenue by Category:\n"
            f"{self.metrics.get('revenue_by_category').round(0)}\n"
            f"\nRevenue by City:\n"
            f"{self.metrics.get('revenue_by_city').round(0)}\n"
            f"Median Revenue per Order: {self.metrics.get('median_revenue'):.0f}\n"
            f"Revenue Standard Deviation: {self.metrics.get('standard_deviation'):.0f}\n"
        )