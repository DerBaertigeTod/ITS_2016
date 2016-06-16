def get_color_name(r,g,b):
	deltas = [0,0,0,0]
	i = 0
	colors ={'Red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,128,0],'blue':[0,0,255],'violett':[238,130,238],'brown':[165,42,42]}
	for c_key, c_val in enumerate(colors):
		 	deltas[i] = c_val[0] - r
		 	deltas[i] += c_val[1] - g
		 	deltas[i] += c_val[2] - b
			i++
	winner = min(deltas, key=deltas.get)

	return colors[winner][0]


get_color_name()	 	
		 	 