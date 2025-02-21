# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    data = pd.read_csv('files/input/shipping-data.csv')
    return data

def create_visual_for_shipping_per_warehouse(data):
    df = data.copy()
    plt.figure(figsize=(10, 5))
    counts = df.Warehouse_block.value_counts()
    counts.plot.bar(
        title='Shipping per Warehouse', 
        color='tab:blue',
        xlabel='Warehouse block',
        ylabel='Record Count',
        fontsize=12)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    os.makedirs('docs', exist_ok=True)
    plt.savefig('docs/shipping_per_warehouse.png')

def create_visual_for_mode_of_shipment(data):
    df = data.copy()
    plt.figure(figsize=(10, 5))
    counts = df.Mode_of_Shipment.value_counts()
    counts.plot.pie(
        title='Mode of Shipment', 
        colors=['tab:blue', 'tab:orange', 'tab:green'],
        ylabel='',
        fontsize=12)
    plt.savefig('docs/mode_of_shipment.png')
    
def create_visual_for_average_customer_rating(data):
    df = data.copy()
    plt.figure(figsize=(10, 5))
    df = (
        df[["Mode_of_Shipment", "Customer_rating"]]
        .groupby("Mode_of_Shipment").describe()
    )
    df
    df.columns = df.columns.droplevel()
    df = df[["mean", "min", "max"]]
    plt.barh(
        y=df.index,
        width=df["max"].values -1,
        left=df["min"].values,
        height=0.9,
        color="lightgray",
        alpha=0.8
    )
    colors = ["tab:green" if x > 3 else "tab:red" for x in df["mean"].values]
    plt.barh(
        y=df.index,
        width=df["mean"].values - 1,
        left=df["min"].values,
        height=0.6,
        color=colors,)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.title("Average Customer")
    plt.savefig("docs/average_customer_rating.png")

def create_visual_for_weight_distribution(data):
    df = data.copy()
    plt.figure(figsize=(10, 5))
    df.Weight_in_gms.plot.hist(
        bins=10,
        color='tab:blue',
        title='Weight Distribution',
        xlabel='Weight (g)',
        ylabel='Record Count',
        edgecolor='black',
        fontsize=12)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig('docs/weight_distribution.png')

def create_dashboard():
    os.makedirs('docs', exist_ok=True)
    with open('docs/index.html', 'w') as file:
        file.write("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Shipping Dashboard</title>
        </head>
        <body>
            <h1>Shipping Dashboard</h1>
            <h2>Shipping per Warehouse</h2>
            <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse" width="800" height="400">
            <h2>Mode of Shipment</h2>
            <img src="mode_of_shipment.png" alt="Mode of Shipment" width="800" height="400">
            <h2>Average Customer Rating</h2>
            <img src="average_customer_rating.png" alt="Average Customer Rating" width="800" height="400">
            <h2>Weight Distribution</h2>
            <img src="weight_distribution.png" alt="Weight Distribution" width="800" height="400">
        </body>
        </html>
        """)

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    
    data = load_data()
    create_visual_for_shipping_per_warehouse(data)
    create_visual_for_mode_of_shipment(data)
    create_visual_for_average_customer_rating(data)
    create_visual_for_weight_distribution(data)
    create_dashboard()

if __name__ == "__main__":
    pregunta_01()