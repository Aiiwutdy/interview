print("====Todolist=====")


def checktasks():
    with open('todolistnew.txt', 'r+') as todolist:
        print('Please enter check your tasks: ', todolist.name)
        tasks = todolist.read()
        print(tasks)

def check1():
    if check_input == '1':
        checktasks()
        print('Thank you')

def check2():
    if check_input == '2':
        task_input = '0'
        while task_input != '':
            task_input = input('Please input your tasks. When entering the number 0 will be saved.: ')
            with open('todolistnew.txt', 'a+') as todolist:
                todolist.write('* ' + task_input + '\n')
            if task_input == '':
                lines = open('todolistnew.txt').readlines()
                open('todolistnew.txt', 'w').writelines(lines[:-1])
                checktasks()
                break
            elif task_input == '0':
                exit(0)
                print('Thank you')

def check3():
    if check_input == '3':
        checktasks()
        while True:
            delete_input = int(input('Which task line do you want to delete? '))
            with open('todolistnew.txt', 'r') as todolist:
                lines = todolist.readlines()
            with open('todolistnew.txt', 'w') as todolist:
                todolist.writelines(lines[:delete_input - 1] + lines[delete_input:])
            checktasks()
            print('Thank you')
            break

def check4():
    if check_input == '4':
        print('Thank you')


print('This is a simple to do list program.')
print('What do you want to do?')
print('1 - Check your tasks')
print('2 - Add your tasks')
print('3 - Delete your tasks')
print('4 - End this program')

check_input = input('Please select 1 / 2 / 3 / 4 : ')
check1()
check2()
check3()
check4()

print("\n==================================================================================================================\n")

print("1.   1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz")
print("     Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz")
print("     41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz")
print("     61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz")
print("     Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz")

def FizzBuZZZ():

    num = 1
    counter = 1
    while (num <= 100):
        if counter % 20 == 1:
            print('')
        if num % 15 == 0:
            print('FizzBuzz', end=' ')
        elif num % 3 == 0:
            print('Fizz', end=' ')
        elif num % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(num, end=' ')
        num += 1
        counter += 1

FizzBuZZZ()

print("\n==================================================================================================================\n")

print("2. 1600 -> true")
print("   2000 -> true")
print("   1500 -> false")
print("   2004 -> true")
print("   2008 -> true")
print("   2010 -> false\n")

def Year(year = 2000):
    if type(year) != int:
        return False
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if __name__ == '__main__':
    testSet = [1600,2000,1500,2004,2008,2010,2016,2012,2020]
    for year in testSet :
        print (year,"->",Year(year))
print("\n==================================================================================================================\n")

print("3.1  n=3   n=4    n=6")
print("     *     *      *")
print("     **    **     **")
print("     ***   ***    ***")
print("           ****   ****")
print("                  *****")
print("                  ******\n")
def NumRight():
    n=int(input("Please enter number(n) : "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('*',end=" ")
        print()
NumRight()

print("\n==================================================================================================================\n")

print("3.2   n=3    n=4      n=6")
print("        *      *        *")
print("       **     **       **")
print("      ***    ***      ***")
print("            ****     ****")
print("                    *****")
print("                   ******\n")

def Switch():
    n = int(input("Please enter number:"))
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("")
Switch()

print("\n==================================================================================================================\n")

print("3.3  n=1    n=2      n=3    	 n=4       n=5")
print("     *       *        *         *         * ")
print("            * *      * * 	   * *       * *")
print("                    *   *	  *   *     *   *")
print("                             *     *   *     *")
print("                                      *       *  \n")

def triangle():
    n = int(input("Please enter Number : "))
    for row in range(1, n+1):
        for col in range(1, 2*n):
            if  row+col==n+1 or col-row==n-1:
                 print("*", end=" ")
            else:
                print(end=" ")
        print()
triangle()

print("\n==================================================================================================================\n")

print("3.4  n=1	n=2	n=3	n=4     n=5")
print("     *	**	* *	*  *	*   *")
print("     	**	 * 	 **      * *")
print("     		* *	 **       *  ")
print("     			*  *	 * *")
print("     					*   *\n")


def pattern():
    num = int(input("Please enter Number : "))
    for i in range(num):
        print("".join("*" if j == i or num - 1 - j == i else " "
                      for j in range(num)))
pattern()

print("\n==================================================================================================================\n")

print("3.5  n=1  n=2  n=3   n=4    n=5        n=9")
print("     *    *     *     *      *          *")
print("          *    ***   ***    ***        ***")
print("                *    ***   *****      *****")
print("                      *     ***      *******")
print("                             *      *********")
print("                                     *******")
print("                                      *****")
print("                                       ***")
print("                                        *\n")

def diamond():
    n = int(input("please enter diamond's height: "))
    for i in range(1, n, 2):
        print(" "*(n//2-i//2), "*"*i)
    for i in range(n, 0, -2):
        print(" "*(n//2-i//2), "*"*i)
diamond()
print("\n==================================================================================================================\n")

print("3.6  n=1		n=2     n=3         n=4")
print("     +       A+B     AA+BB       AAA+BBB")
print("             +E+     A+E+B       AA+E+BB")
print("             C+D  	+EEE+       A+EEE+B")
print("                     C+E+D       +EEEEE+")
print("                     CC+DD       C+EEE+D	")
print("                                 CC+E+DD")
print("                                 CCC+DDD\n")

def ABCDE():
    number = int(input('Please input number (n): '))
    column = number * 2 - 1
    center = number - 1

    for i in range(0, center + 1):
        for j in range(0, column):
            if j == center - i or j == center + i:
                print(end='+')
            elif i + j <= center - 1:
                print(end='A')
            elif j - i > center:
                print(end='B')
            else:
                print(end='E')
        print()

    for i in range(center - 1, -1, -1):
        for j in range(0, column):
            if j == center - i or j == center + i:
                print(end='+')
            elif j < center - i:
                print(end='C')
            elif j > center + i:
                print(end='D')
            else:
                print(end='E')
        print()

ABCDE()

print("\n==================================================================================================================\n")

print("Medium : 20 -> 2 3 5 7 11 13 17 19\n")

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def printPrime(n):
    for i in range(2, n + 1):
        if isPrime(i):
            print(i, end=" ")

if __name__ == "__main__":
    n = int(input("Please enter number: "))
    printPrime(n)


print("\n==================================================================================================================\n")