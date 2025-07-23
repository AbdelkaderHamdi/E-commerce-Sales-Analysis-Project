import pandas as pd 

def category_performance(df):
    return df.groupby('product_category').agg(
        total_revenue=('final_amount', 'sum'),
        avg_revenue=('final_amount', 'mean'),
        total_orders=('order_id', 'count'),
        total_quantity=('quantity', 'sum')
    ).reset_index()


def month_performance(df):
    return df.groupby('order_month').agg(
        total_revenue=('final_amount', 'sum'),
        avg_revenue=('final_amount', 'mean'),
        total_orders=('order_id', 'count')
    ).reset_index()


def region_performance(df):
    return df.groupby('customer_region').agg(
    total_revenue=('final_amount', 'sum'),
    avg_revenue=('final_amount', 'mean'),
    total_customers=('customer_id', 'count'),
    total_orders=('order_id', 'count')
    ).reset_index()


def groupAge(age):
    if age >= 18 and age <= 25:
        return '18-25'
    elif age >= 26 and age <= 35:
        return '26-35'
    elif age >= 36 and age <= 45:
        return '36-45'
    elif age >= 46 and age <= 55:
        return '46-55'
    elif age >= 56:
        return '56+'

def age_group_performance(df): 
    df['age_groups'] = df['customer_age'].apply(groupAge)
    return df.groupby('age_groups').agg(
    total_revenue=('final_amount', 'sum'),
    avg_order_value=('final_amount', 'mean'),
    unique_customers=('customer_id', 'count'),
    avg_quantity_per_order=('quantity', 'mean')
).reset_index()


def discount_Analysis(df):
    discount_analysis = df.groupby('discount_applied').agg(
    avg_order_value=('final_amount', 'mean'),
    total_revenue=('final_amount', 'sum'),
    num_orders=('order_id', 'count')
    ).reset_index()
    discount_analysis['revenue_per_order']= (discount_analysis['total_revenue']/discount_analysis['num_orders']).round(2)
    return discount_analysis



def top_ten_products(df):
    top_10_products = df.groupby('product_name')['final_amount'].sum().nlargest(10).reset_index()
    top_10_products.columns = ['product_name', 'total_revenue']
    return top_10_products


def top_ten_customers(df):
    top_10_customers = df.groupby('customer_id')['final_amount'].sum().nlargest(10).reset_index()
    top_10_customers.columns = ['customer_id', 'total_revenue_spent']
    return top_10_customers