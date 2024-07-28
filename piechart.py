import matplotlib.pyplot as pit

Data to plot

labels 'Labell', 'Label2', 'Label3', 'Label4"]

sizes [15, 30, 45, 10] These are the sizes or proportions of eachistice

colors['gold", "yellowgreen', 'Lightcoral, Lightskyblue] explode (0.1, 0, 0, 0) Explode the Ist slice (Le. Label

Create a ple chart

plt.ple(sizes, explode explode, labels labels, colors colors, autopct=%1.1fW, shadow True, startangle-148)

OUTPUT

Equal aspect ratio ensures that pie ts drawn as a circle

plt.axis("equal)

Add a title

plt.title( 'My Pie Chart')

Display the chart

plt.show()