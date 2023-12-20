def interpolation(d, x):
	output = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0]))

	return output

#[x, y]
data=[[2019, 12124],[2021, 5700]]

year_x=2020

# Finding the interpolation
print(interpolation(data, year_x))
