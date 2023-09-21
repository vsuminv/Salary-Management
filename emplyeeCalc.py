def emplyeeCalc(emplyee):
    
    guyeo = 0
    segum = 0
   
   
    
    
    if emplyee['ho'] == 1 and emplyee['gub'] == 1:
        guyeo = 95000
    elif emplyee['ho'] == 1 and emplyee['gub'] == 2:
        guyeo = 80000
    elif emplyee['ho'] == 2 and emplyee['gub'] == 1:
        guyeo = 92000
    elif emplyee['ho'] == 2 and emplyee['gub'] == 2:
        guyeo = 75000
    elif emplyee['ho'] == 3 and emplyee['gub'] == 1:
        guyeo = 89000
    elif emplyee['ho'] == 3 and emplyee['gub'] == 2:
        guyeo = 70000
    elif emplyee['ho'] == 4 and emplyee['gub'] == 1:
        guyeo = 86000
    elif emplyee['ho'] == 4 and emplyee['gub'] == 2:
        guyeo = 65000
    elif emplyee['ho'] == 5 and emplyee['gub'] == 1:
        guyeo = 83000
    elif emplyee['ho'] == 5 and emplyee['gub'] == 2:
        guyeo = 60000
    else:
        guyeo = 0
    
    gigub  = guyeo + emplyee['salary']
    
    
    
    
   
        
    if gigub >= 90000:
        segum = (gigub*0.012)-1000
    elif 80000 <= gigub <= 89999:
        segum = (gigub*0.007)-500
    elif 70000 <= gigub <= 79999:
        segum = (gigub*0.005)-300
    else:
        segum = (gigub*0)-0
        
   
    chain = gigub - segum
    
    emplyee['segum'] = int(segum)
    emplyee['chain'] = int(chain)
    emplyee["guyeo"] = guyeo
    emplyee['gigub'] = gigub
    
   
    
    
    
     
        
        
    
        
        
    
        
    
        
    