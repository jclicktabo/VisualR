import csv 
import plotly.plotly as py
import plotly.graph_objs as go

with open('voucher.csv') as csvfile:
     reader = csv.reader(csvfile, delimiter= ";")
     for row in reader:
        eins = row[1]
        zwei = row[2]




trace = go.Table(
    header=dict(values=['A Scores', 'B Scores']),
    cells=dict(values=[[100, 90, 80, 90],
                       [95, 85, 75, 95]]))

data = [trace] 
py.iplot(data, filename = 'basic_table')
        
        # print(row[1])