def WinFunctionThreeBLACK(z):
    
    q = 0
    
    f , g , h , j = z[q] , z[q+1] , z[q+2] , z[q+3]
    
    w = -1
    
    v = 0
    
    win = False
    while q!= 4:
        
        while w != len(f)-1 and len(f) > v and len(g) > v + 1 and len(h) > v + 2 and len(j) > v + 3:

            w += 1
            v += 1
            
            y =  f[w]
            if y[1] == "B":
                  
                y = g[w+1]
                if y[1] == "B":
                      
                    y = h[w+2]
                    if y[1] == "B":
                          
                        y = j[w+3]
                        if y[1] == "B":
                              
                            return "win"       
        v = 0
        w = -1                                              
        q += 1        
        if q != 4:                   
            f , g , h , j = z[q] , z[q+1] , z[q+2] , z[q+3]
                          
                          
def WinFunctionThreeRED(z):
    
    q = 0
    
    f , g , h , j = z[q] , z[q+1] , z[q+2] , z[q+3]
    
    w = -1
    
    v = 0
    
    win = False
    while q!= 4:
        
        while w != len(f)-1 and len(f) > v and len(g) > v + 1 and len(h) > v + 2 and len(j) > v + 3:

            w += 1
            v += 1
            
            y =  f[w]
            if y[1] == "R":
                  
                y = g[w+1]
                if y[1] == "R":
                      
                    y = h[w+2]
                    if y[1] == "R":
                          
                        y = j[w+3]
                        if y[1] == "R":
                        
                            return "win"       
        v = 0
        w = -1                                              
        q += 1        
        if q != 4:                   
            f , g , h , j = z[q] , z[q+1] , z[q+2] , z[q+3]
                          
                          
       
     
    