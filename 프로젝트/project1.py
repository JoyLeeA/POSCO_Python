def menubox(): #메뉴박스 호출 함수
    print("%-15s %-18s %-11s %-9s %-10s %-10s" %("Student", "Name", "Midterm", "Final", "Average", "Grade"))
    print("----------------------------------------------------------------------------")

def Avg(a, b): #평균 계산 함수
    return (a + b) / 2 

def Grade(avg): # 등급 계산 함수
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def show (a) : #show 함수
    menubox()
#     print(a)
    sorted_s1 = sorted(stu_dict.items(), key =lambda a: a[1][4], reverse = True)
#     print(sorted_s1)
    for st in sorted_s1:
#         print(st)
        print("%-15s %-20s %-10d %-10d %-10s %-10s" %(st[1][0], st[1][1], st[1][2] , st[1][3] ,st[1][4], st[1][5]))
#         print(sorted_s1)
    

def search(a): #search 함수
    stnum = input("Student ID: ")
    for i in a:
        if i == stnum:
            menubox()
            print("%-15s %-20s %-10d %-10d %-10s %-10s" %(a[i][0],  a[i][1], a[i][2] , a[i][3] ,a[i][4], a[i][5]))
            return
    print('NO SUCH PERSON')

def changescore(a): # changescore 함수

    stnum = input("Student ID: ")
    for i in a:
        if i == stnum:
            MF = input("Mid/Final? ").lower()
            if MF == 'mid':
                newscore = int(input("Input new score: "))
                if 0> newscore or newscore>100 :
                    return
                menubox()
                print("%-15s %-20s %-10d %-10d %-10s %-10s" %(a[i][0],  a[i][1], a[i][2] , a[i][3] ,a[i][4], a[i][5]))
                print('Score changed')
                a[i][2] = newscore
            elif MF == 'final' :
                newscore = int(input("Input new score: "))
                if 0 > newscore or newscore > 100:
                    return
                menubox()
                print("%-15s %-20s %-10d %-10d %-10s %-10s" %(a[i][0],  a[i][1], a[i][2] , a[i][3] ,a[i][4], a[i][5]))
                print('Score changed')
                a[i][3] = newscore
            else :
                return
            a[i][4] = Avg(a[i][2],a[i][3])
            a[i][5] = Grade(a[i][4])
            print("%-15s %-20s %-10d %-10d %-10s %-10s" %(a[i][0],  a[i][1], a[i][2] , a[i][3] ,a[i][4], a[i][5]))
            return
    print('NO SUCH PERSON')

def add (a) : #add 함수, 학번을 스트링으로 입력받으므로 문자열도 삽입가능
    stnum = input("Student ID: ")
    for i in a:
        if i == stnum:
            print('ALREADY EXISTS')
            return
    name = input('Name : ')
    mid = int(input('Midterm Score : '))
    if 0 > mid or mid > 100:
        return
    fin = int(input('Final Score : '))
    if 0 > fin or fin > 100:
        return
    avg = Avg(mid,fin)
    stu_dict[stnum] = [stnum, name, mid ,fin ,avg ,Grade(avg)]

    print('Studnet added')

def searchgrade(a) : #searchgrade 함수
    grade = input('Grade to search: ').upper()
    if grade not in ['A','B','C','D','F'] :
        return
    flag = False
    for i in a :
        if a[i][5] == grade :
            print("%-15s %-20s %-10d %-10d %-10s %-10s" %(a[i][0],  a[i][1], a[i][2] , a[i][3] ,a[i][4], a[i][5]))
            flag = True
    if not flag :
        print('NO RESULTS')

def remove(a) : #remove 함수
    if  len(a) == 0 :
        print('List is empty')
        return
    stnum = input("Student ID: ")
    for i in range(len(a)):
        if stnum in a:
            a.pop(stnum)
            print('Student removed')
            # print(a)
            return

    print('NO SUCH PERSON')

def quit(a) : #quit 함수
    #save = input('Save data?[yes/no]').lower()
    #if save == 'yes' :
        filename = input('Filename : ')
        f1 = open(filename, "w")
        for i in a :
            s = '%s\t%s\t%d\t%d\n'%(a[i][0],a[i][1],a[i][2],a[i][3])
            f1.write(s)
        f1.close()

stu_dict = {} #전역 변수 딕셔너리 선언

def main() :
    f = open("students.txt", "r")

    for x in f:
        stu_dict[x.split()[0]] = [x.split()[0], x.split()[1] + " " + x.split()[2], int(x.split()[3]), int(x.split()[4]),
                                  (Avg(int(x.split()[3]), int(x.split()[4]))),
                                  Grade((Avg(int(x.split()[3]), int(x.split()[4]))))]
    f.close()
    show(stu_dict) #시작시 불러온 정보 출력을 위해 show함수 호출
    while True :
        c = input('#').lower()

        if c == 'show' :
            show(stu_dict)
        elif c == 'search' :
            search(stu_dict)
        elif c == 'changescore' :
            changescore(stu_dict)
        elif c == 'add' :
            add(stu_dict)
        elif c == 'searchgrade' :
            searchgrade(stu_dict)
        elif c == 'remove' :
            remove(stu_dict)
        elif c == 'quit' :
            save = input('Save data?[yes/no]').lower()
            if save == 'yes' :
                quit(stu_dict)
                break
            elif save == 'no':
                break
            else:
                pass

if __name__ == "__main__":
    main()
