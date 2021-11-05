import plotly.express as px
import csv
import numpy as np

with open("marks.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = 'Marks In Percentage', y = 'Days Present')
    fig.show()

def getData(data_path):
    marks = []
    days = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            marks.append(float(row['Marks In Percentage']))
            days.append(float(row['Days Present']))

    return {'x': days, 'y': marks}

def findCorr(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print(correlation)

def setup():
    data_path = "marks.csv"
    datasource = getData(data_path)
    findCorr(datasource)

setup()