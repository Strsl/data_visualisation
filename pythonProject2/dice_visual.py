from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for _ in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
for n in range(2, die_3.num_sides + die_2.num_sides + die_1.num_sides + 1):
    frequancy = results.count(n)
    frequencies.append(frequancy)

x_values = list(range(3, die_3.num_sides+die_2.num_sides+die_1.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling two D6 dice 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')