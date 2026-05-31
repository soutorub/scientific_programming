from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    df = pd.read_csv(os.path.join(BASE_DIR, '..', 'apartments_data_enriched_cleaned.csv'))
    df['id'] = range(1, len(df) + 1)

    # KPIs
    number_of_apartments = df.shape[0]
    mean_price = f"{df['price'].mean():.2f}"
    median_price = f"{df['price'].median():.2f}"
    mean_area = f"{df['area'].mean():.2f}"

    # Interactive Plotly histogram
    fig = px.histogram(
        df, x='price', nbins=20,
        labels={'price': 'Price (CHF)', 'count': 'Number of Apartments'},
    )
    fig.update_traces(marker_color='#38bdf8', marker_line_color='#0f172a', marker_line_width=1)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#94a3b8', size=13),
        title=dict(text='Price Distribution of Apartments', font=dict(color='#e2e8f0', size=18)),
        xaxis=dict(title='Price (CHF)', gridcolor='#1e293b', linecolor='#334155'),
        yaxis=dict(title='Number of Apartments', gridcolor='#1e293b', linecolor='#334155'),
        margin=dict(l=40, r=40, t=60, b=40),
    )
    chart_html = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')

    apartments = df.to_dict(orient='records')

    return render_template(
        'index.html',
        apartments=apartments,
        number_of_apartments=number_of_apartments,
        mean_price=mean_price,
        median_price=median_price,
        mean_area=mean_area,
        chart_html=chart_html,
    )

if __name__ == '__main__':
    app.run(debug=True)
