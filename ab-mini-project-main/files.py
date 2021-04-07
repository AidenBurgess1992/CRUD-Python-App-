

#with open('data/product.txt', 'r') as f:
    #f_contents = f.read() 
    #print(f_contents)


#with open('data/product.txt', 'r') as f:
    #f_contents = f.readlines() 
    #print(f_contents, end='')
    
    
#with open('data/product.txt', 'r') as f:
    
    #for line in f:
        #print(line, end='')


with open('data/product.txt', 'r') as rf:
    with open('data/_copyproduct.txt', 'w') as wf:
        for line in rf: # for each line in orginal write to wf
            wf.write(line) # Copies entire file into a new one. 