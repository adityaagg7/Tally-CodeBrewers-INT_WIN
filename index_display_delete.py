from prettytable import PrettyTable
import os
def main(files):
    m={}
    i=0
    table =PrettyTable()
    table.field_names=['Index','Size','FilePath']
    for path,size in files:
        m[i]=(path,size)
        table.add_row([i,m[i][1],m[i][0]],divider=True)
        i+=1        

    while 1:
        print(table)
        inp=input("\nEnter the comma-separated indices of the files to be deleted or leave empty to exit:   ") 
        
        if len(inp)==0: 
            break
        indices=inp.split(',')
        for index in indices:
            if os.path.exists(m[int(index)][0]):
                os.remove(m[int(index)][0])
                table=table.del_row(int(index))
                print(table)
                print("Deleted ",m[int(index)][0],"\n")
            else:
                print(f"File {m[int(index)][0]} not found \n")
            

        
            
main([('/home/gsuare/Desktop/hi/subdir/h2.txt', 24),('/home/gsuare/Desktop/hi/h1.txt', 77)])
        
        
        