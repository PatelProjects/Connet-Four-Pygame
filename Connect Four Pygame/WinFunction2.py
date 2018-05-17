#checks rows

def lowest(q):
    
    p = 100
    
    for i in q:
        if len(i) < p:
            p = len (i)
            
    return p 

  
def WinFunctionTwoRED(a):
    b = 0 
    
    f , g , h , j = a[b] , a[b+1] , a[b+2] , a[b+3]
    l = [f , g , h , j]
    
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
                     
                    if e == 4:
                        return "win"
                        e = 0
                 
                else:
                    e = 0 
            
            e = 0
                    
        skip = False
        
        if b != 3:
            b += 1
            f , g , h , j = a[b] , a[b+1] , a[b+2] , a[b+3]
            l = [f , g , h , j]
            d = lowest(l)
            

def WinFunctionTwoBLACK(a):
    b = 0 
    
    f , g , h , j = a[b] , a[b+1] , a[b+2] , a[b+3]
    l = [f , g , h , j]
    
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
    
                 
                if m[1] == "B":
                    e += 1
                     
                    if e == 4:
                        return "win"
                        e = 0
                 
                else:
                    e = 0 
                    
            e = 0
                    
        skip = False
        
        if b != 3:
            b += 1
            f , g , h , j = a[b] , a[b+1] , a[b+2] , a[b+3]
            l = [f , g , h , j]
            d = lowest(l)

            
    