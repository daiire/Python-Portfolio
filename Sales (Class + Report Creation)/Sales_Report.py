import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statsmodels



class SalesReport:
    def __init__(self, input_path="Portfolio/Data/sales_data.csv", output_path="Portfolio/Data/trimmed_data.csv"):
        self.input = input_path
        self.output = output_path
        self.clean_data = None
        self.data = None
        self.report_dates = "Portfolio/Reports/Top_Dates_Report.csv"
        self.report_order_status = "Portfolio/Reports/Order_Status_Report.csv"
        self.report_sales_region = "Portfolio/Reports/Regional_Sales_Report.csv"
        self.report_us_states = "Portfolio/Reports/US_States_Report.csv"
        self.report_chart = "Portfolio/Reports/Chart_Report.html"

    def load_data(self):
        try:
            self.data = pd.read_csv(self.input, encoding='ISO-8859-1')
        except FileNotFoundError:
            print("The file inventory.csv was not found.")
        except pd.errors.EmptyDataError:
            print("The file is empty.")

    def process_data(self):
        df = self.data
        columns_to_drop = ['phone', 'address_line_1', 'address_line_2', 'contact_first_name', 'contact_last_name',
                           'online_order_number', 'postal_code']
        df_drop = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

        df_drop['territory'] = df_drop['territory'].replace('Japan', 'APAC')
        df_drop['territory'] = df_drop['territory'].fillna('North America')
        df_drop['order_date'] = pd.to_datetime(df_drop['order_date']).dt.date
        df_drop['total_sales'] = df_drop['quantity_ordered'] * df_drop['price_each']
        df_drop.rename(columns={'territory': 'region'}, inplace=True)

        self.clean_data = df_drop
        df_drop.to_csv(self.output, index=False)
        return self.clean_data

    def create_report(self):
        clean_data = self.clean_data

        report_top_dates = (
            clean_data
            .groupby('order_date')
            .agg(total_sales=('total_sales', 'sum'), order_count=('order_id', 'count'))
            .sort_values(by='total_sales', ascending=False)
            .assign(total_sales=lambda df: df['total_sales'].apply(lambda s: f'${s:,.2f}'))
            .rename(columns={'total_sales': 'Total Sales', 'order_count': 'Order Count'})
        ).head(10)

        report_order_status = (
            clean_data
            .groupby('status')
            .agg(order_count=('order_id', 'count'))
            .rename(columns={
                'order_count': 'Order Count'})
        )

        region_sales = clean_data.groupby(['region', 'country']).agg(
            total_sales=('total_sales', 'sum'),
            order_count=('order_id', 'count'))
        region_totals = region_sales.groupby(level='region').sum()

        region_totals['country'] = 'REGIONAL TOTAL'
        region_totals = region_totals.set_index('country', append=True)

        report_sales_region = ((pd.concat([region_sales, region_totals])
                                .sort_values(by=['region', 'total_sales'], ascending=[True, False]))
                               .assign(total_sales=lambda df: df['total_sales'].apply(lambda s: f'${s:,.2f}'))
                               .rename(columns={'total_sales': 'Total Sales', 'order_count': 'Order Count'})
                               )

        report_top_states = (
            clean_data[clean_data.country == 'USA']
            .groupby('state')
            .agg(total_sales=('total_sales', 'sum'), order_count=('order_id', 'count'))
            .sort_values(by='total_sales', ascending=False)
            .assign(total_sales=lambda df: df['total_sales'].apply(lambda s: f'${s:,.2f}'))
            .rename(columns={'total_sales': 'Total Sales', 'order_count': 'Order Count'})
        )

        report_top_dates.to_csv(self.report_dates, index=True)
        report_order_status.to_csv(self.report_order_status, index=True)
        report_sales_region.to_csv(self.report_sales_region, index=True)
        report_top_states.to_csv(self.report_us_states, index=True)

    def create_chart(self):
        df = self.clean_data

        sales_by_product = df.groupby('product_line')['total_sales'].sum().reset_index()
        order_count = df.groupby('product_line')['order_id'].count().reset_index()
        x_labels = [label.replace(' ', '<br>') for label in sales_by_product['product_line']]

        chart = go.Figure()
        chart.add_trace(go.Bar(
            x=x_labels,
            y=sales_by_product['total_sales'], customdata=order_count['order_id'],
            marker_color='rgb(55, 83, 109)',
            text=sales_by_product['total_sales'],
            textposition='auto'
        ))

        chart.update_layout(xaxis_title="Product Line",
                            yaxis_title="Total Sales (US$)",
                            title=dict(text="Sales Report",
                                       subtitle=dict(
                                           text="Total Sales by Product Line",
                                           font=dict(color="gray", size=13))),
                            barmode="stack",
                            legend_traceorder='normal',
                            )
        chart.update_traces(texttemplate='$%{text:,.2f}<br>Order Count:<br>%{customdata}', textposition='outside')

        chart.write_html(self.report_chart)

    def run(self):
        self.load_data()
        self.process_data()
        self.create_report()
        self.create_chart()
