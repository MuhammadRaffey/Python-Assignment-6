def manage_student_database()->None:
    nameList:list[tuple]=[]
    id:int=1
    while True:
        nameInp:str=input("Enter your name: ")
        if nameInp=="stop":
            break
        if  any(nameInp == name for _, name in nameList):
            print("This name is already in the list.")
        else:
            nameTup:tuple=(id,nameInp)
            nameList.append(nameTup)
            id+=1
            # print(id)
    print("Complete list of students(Tuples): ",nameList)
    print("List of students with IDs: ")
    for id,name in nameList:
        print("ID: ",id,", Name: ",name)
    print("Total number of students: ",len(nameList))
    print("Total length of all student names combined: ",sum(len(name) for _, name in nameList))
    print("The student with the longest name is:", max(nameList, key=lambda x: len(x[1]))[1])
    print("The student with the shortest name is:", min(nameList, key=lambda x: len(x[1]))[1])

manage_student_database()