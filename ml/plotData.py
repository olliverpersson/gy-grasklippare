import plotly.express as px
import json

with open('data.json') as json_file:
	data = json.load(json_file)

print(data)
print( type(data) )



fig = px.scatter_3d(data, x='r', y='g', z='b', color='t')
fig.show()
