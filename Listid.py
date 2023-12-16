import random

#
def work1():
    print("\n---------1---------\n")
#
def work2():
    print("\n---------2---------\n")
    # print(test._set)

def work3():
    print("\n---------3---------\n")

    level43=[12,1,5,10,14,1,2]

    for x in level43:
        print("*"*x)

def work4():
    print("\n---------4---------\n")

    while True:
        ZipCode=str(input("Enter a zip code: "))
        
        if ZipCode.isdigit() and len(ZipCode) == 5 and ZipCode[0] != "0":
            break
        else:
            print("ERROR! ENTER VALID CODE")

    if ZipCode[0] == '1':
        status = "Tallinn"
    elif ZipCode[0] == '2':
        status = "Narva, Narva-Jõesuu"
    elif ZipCode[0] == '3':
        status = "Kohtla-Järve"
    elif ZipCode[0] == '4':
        status = "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa"
    elif ZipCode[0] == '5':
        status = "Tartu linn"
    elif ZipCode[0] == '6':
        status = "Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
    elif ZipCode[0] == '7':
        status = "Viljandimaa, Järvamaa, Harjumaa, Raplamaa"
    elif ZipCode[0] == '8':
        status = "Pärnumaa"
    elif ZipCode[0] == '9':
        status = "Läänemaa, Hiiumaa, Saaremaa"
    else:
        status = "ERROR!"
        
    print(f"\nZIPCODE = {status}")
    if int(ZipCode[0]) <= 3 and int(ZipCode[0]) != 0:
        print("Оставайтесь дома!")
    else:
        print("Носите маски!")

def work5():
    print("\n---------5---------\n")
    work42=str(input("Enter a work: "))
    list_work42=list(work42)
    list_work42.insert(0,list_work42[-1])
    list_work42.insert(-1,list_work42[1])
    list_work42.pop(1)
    list_work42.pop(-1)
    print(list_work42)
    
    x1 = int(input("X a number: "))-1

    x2 = int(input("X a number: "))-1

    if (x1 < int(len(work42)/2) and x2 >= int(len(work42)/2)):
        number0 = 1
        number1 = 1
    elif (x1 >= int(len(work42)/2) and x2 < int(len(work42)/2)):
        number0 = 2
        number1 = 0

    print(list_work42[x1])
    print(list_work42[x2])

    temp = list_work42[x1]
    list_work42.insert(x1,list_work42[x2])    
    list_work42.insert(x2+1,temp)        
    list_work42.pop(x1+number0)
    list_work42.pop(x2+number1)

    print(list_work42) 

def work6():
    print("\n---------6---------\n")
    kokku = random.randint(2,20)
    print(kokku)
    num_list = []
    for x in range(kokku):
        num_list.append(round( x*1000 ,2))
    print(num_list)
    MaxNumList=max(num_list)
    n=num_list.index(MaxNumList)
    print(f"Max={MaxNumList} at {n}")
    num_list.pop(n)
    MaxNumList = MaxNumList/len(num_list)
    num_list.insert(n,MaxNumList)
    print(num_list)

def work7():
    print("\n---------7---------\n")

    kokku = random.randint(0,32)
    numberList = []

    for x in range(kokku):
        numberList.append( random.randint( -100, 100) )
    print(numberList)
    for x in range(len(numberList)):
        numberList[x] = abs(int(numberList[x]))

    numberList.sort(reverse=True)
    print( numberList )

def work8():
    print("\n---------8---------\n")
    list1 = ['крот', 'белка', 'выхухоль']
    list2 = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
    list3 = ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']

    print(list1)
    print(list2)
    print(list3)

    MAXlist1 = len(max(list1, key=len))
    for x in range(len(list1)):
        if len(list1[x]) < MAXlist1:
            list1[x] += "_" * ( MAXlist1 - len(list1[x]) )

    MAXlist2 = len(max(list2, key=len))
    for x in range(len(list2)):
        if len(list2[x]) < MAXlist2:
            list2[x] += "_" * ( MAXlist2 - len(list2[x]) )

    MAXlist3 = len(max(list3, key=len))
    for x in range(len(list3)):
        if len(list3[x]) < MAXlist3:
            list3[x] += "_" * ( MAXlist3 - len(list3[x]) )

    print()
    print(list1)
    print(list2)
    print(list3)
#
def work9():
    print("\n---------9---------\n")
#
def work10():
    print("\n---------10---------\n")

def work11():
    print("\n---------11---------\n")

    järjendi0 = ['a','b','c','d','e','f']
    järjendi1 = []

    for x in range(len(järjendi0)-1):
        järjendi1.append(järjendi0[x]*(x+1))

    print(järjendi1)
#
def work12():
    print("\n---------12---------\n")
#
def work13():
    print("\n---------13---------\n")
#
def work14():
    print("\n---------14---------\n")

def work15():
    print("\n---------15---------\n")

    EestiKeel = ['üks', 'kaks', 'kolm', 'neli']
    IngliseKeel = ['one', 'two', 'three', 'four']
    ItaaliaKeel = ['uno', 'due', 'tre', 'quattro']

    for x in range(4):
        print(f" {x+1} {EestiKeel[x]} - {IngliseKeel[x]} - {ItaaliaKeel[x]}")
#
def work16():
    print("\n---------16---------\n")
#?
def work17():
    print("\n---------17---------\n")
    sona="automobiil"
    answer = str(input("auto:"))
    if answer in sona:
        print("Jaa, sisaldab sõna")
#? come up a task
def work18():
    print("\n---------18---------\n")

work1()
work2()
work3()
work4()
work5()
work6()
work7()
work8()
work9()
work10()
work11()
work12()
work13()
work14()
work15()
work16()
work17()
work18()