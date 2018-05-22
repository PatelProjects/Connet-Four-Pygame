from WinFunction2 import * 
import random

def ai(a):
    
    # Checks Collums
    
    y = 0
    x = 0
    counted = False
    for i in a:
        x += 1
        y = 0 
        for j in i:
            if j[1] == "R":
                y += 1
                if y == 3:
                    
                    t = i
                    z = j
                    m = x
                    counted = True
                
            else:
                y = 0
                
    w = 0 
    if counted == True:   
    
        for k in reversed(t):
            if k[1] == "R":
                w += 1
                
            else:
                break
                
            if w == 3:
                return m
            
                
                
                
    
    #Checks Rows
    b = 0 
    
    f , g , h = a[b] , a[b+1] , a[b+2]
    l = [f , g , h ]
    
    e = 0 
    x = 0
    
    d = lowest(l)
    
    skip = False

    
    
    while x != 4:
        
        if d <= 0:
            skip = True
        
        x += 1
        
        if skip == False:
            for i in l:
                 
                m = i[d-1]
    
                if m[1] == "R":
                    e += 1
                     
                    if e == 3:
                        if len(a[x+2]) == d-1:
                            return x+3
                        
                        if len(a[x-2]) == d-1:
                            return x - 1
                 
                else:
                    e = 0 
            
            e = 0
                    
        skip = False
        
        if b != 3:
            b += 1
            f , g , h = a[b] , a[b+1] , a[b+2]
            l = [f , g , h]
            d = lowest(l)
            
            
            
            
            
            
            
            
    #Checks Diagonals (upwards)
    q = 0
    
    f , g , h = a[q] , a[q+1] , a[q+2]
    
    w = -1
    
    v = 0
    
    win = False
    while q!= 4:
        
        while w != len(f)-1 and len(f) > v and len(g) > v + 1 and len(h) > v + 2:

            w += 1
            v += 1
            
            y =  f[w]
            if y[1] == "R":
                  
                y = g[w+1]
                if y[1] == "R":
                      
                    y = h[w+2]
                    if y[1] == "R":
                    
                        
                        if len(a[q-1]) == w-1:
                            return q
                        
                        if len(a[q+3]) == w + 3:
                            return q + 4
                    
        v = 0
        w = -1                                              
        q += 1        
        if q != 4:                   
            f , g , h = a[q] , a[q+1] , a[q+2]
            
            
            
            
            
    
    
    
    #Checks Diagonals (Downwards)
    q = 0
    
    g , h , j = a[q] , a[q+1] , a[q+2]
    
    w = -1
    
    v = 0
    
    win = False
    while q!= 4:

        while w != len(j)-1 and len(j) > v and len(h) > v + 1 and len(g) > v + 2:

            w += 1
            v += 1
                
                  
            y = g[w+2]
            if y[1] == "R":
                  
                y = h[w+1]
                if y[1] == "R":
                      
                    y = j[w]
                    if y[1] == "R":
                        
                        if len(a[q-1]) == w+3:
                            return q
                        
                        if len(a[q+3]) == w-1:
                            return q + 4   
                                                       
        q += 1   
        v = 0
        w = -1     
        if q != 4:                       
            g , h , j = a[q] , a[q+1] , a[q+2]
            

    return random.randint(1,7)
