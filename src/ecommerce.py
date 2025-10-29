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

    def make_the_plots(self):
        self.plots["revenue_by_category"] = plot_revenue_by_category(self.df)
        self.plots["sales_over_time"] = plot_sales_over_time(self.df)

    def summary(self):
        return f"Total Revenue: {self.metrics.get('total_revenue'):.0f}\n"