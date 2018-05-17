#checks collums


def WinFunctionOneRED(v):
	y = 0
	for i in v:
	    y = 0 
	    for j in i:
	        if j[1] == "R":
	            y += 1
	            if y == 4:
	                return "win"
	        else:
	            y = 0


def WinFunctionOneBLACK(v):
	y = 0
	for i in v:
	    y = 0 
	    for j in i:
	        if j[1] == "B":
	            y += 1
	            if y == 4:
	                return "win"
	
	        else:
	            y = 0
