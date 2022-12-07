#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a and not tuple_b:
        return
    if not tuple_a or not tuple_b:                                                                                                 
        return tuple_a[:2] or tuple_b[:2] if len(tuple_a) >= 2 or len(tuple_b) >= 2 else tuple_a or tuple_b
                                                                                                                                   
    a, b = 0, 0                                                                                                                    
    if len(tuple_a) < 2 or len(tuple_b) < 2:                                                                                                 
        if len(tuple_a) < 2 and len(tuple_b) < 2:                                                                                            
            a += tuple_a[0] + tuple_b[0]                                                                                           
        elif len(tuple_a) < 2:                                                                                                          
            a += tuple_a[0] + tuple_b[0]                                                                                           
            b += tuple_b[1]                                                                                                        
        else:                                                                                                                      
            a += tuple_a[a] + tuple_b[0]                                                                                           
            b += tuple_a[1]                                                                                                        
                                                                                                                                   
    else:                                                                                                                          
        a += tuple_a[0] + tuple_b[0]                                                                                               
        b += tuple_a[1] + tuple_b[1]                                                                                               
                                                                                                                                   
    return a, b 
