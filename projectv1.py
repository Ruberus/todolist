#keep the while loop running asking users for tasks
#make your print statements more descriptive for the users
#add numbers next to the tasks(?)


while True:
    opt=int(input('What do you want to do?\n1. Add tasks\n2. View tasks\n3. Remove a task\n4. Mark task as done: '))

    def create():
        with open('projectlol.txt','a+',encoding="utf-8") as fi:
            task=input('Enter your task:')
            fi.writelines(['[ ] ',task,'\n'])


    def view():
        try:
            with open('projectlol.txt','r',encoding="utf-8") as fi:
                fi.seek(0,0)
                fir=fi.read()
                print(fir)
        except FileNotFoundError:
            print("please add tasks before viewing them")
            
            

    def deltask():
        opt2=int(input("enter the task number you want to delete: "))
        with open('projectlol.txt','r',encoding="utf-8") as fi:
            fi.seek(0,0)
            fir=fi.readlines()
        fir.remove(fir[opt2-1])
    
        with open('projectlol.txt','w',encoding="utf-8") as fi:
            fi.writelines(fir)
        

    def mark():
        opt2=int(input("enter the task that is done: "))
        with open('projectlol.txt','r',encoding="utf-8") as fi:
            fi.seek(0,0)
            fir=fi.readlines()
            newopt=''
        try:
            for i in fir[opt2-1]:
                if i=='[' or i==']':
                    continue
                else:
                    newopt=newopt+i
        
        
            another ="[" + "✓" + "]" + newopt

            del fir[opt2-1]
            fir.append(another)
            
        except IndexError:
            print("please specify the correct position of the task in your list")
    
        with open('projectlol.txt','w',encoding="utf-8") as fi:
            fi.writelines(fir)
    
    
   

        
                

    if opt!=1 and opt!=2 and opt!=3 and opt!=4:
        print("please choose a valid option")
    elif opt==1:
            view()
            create()
            view()
    elif opt==2:
        view()
    elif opt==3:
        deltask()
        view()
    elif opt==4:
        mark()
        view()

    opt3=input('Do you want to end the program? Y/N:')
    if opt3=='Y' or opt3=='y':
        break
