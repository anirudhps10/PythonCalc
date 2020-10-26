#Python Program to Find Numbers Divisible by Another Number

# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,15,48,48,95,92,632,3,1,231,231,23,123,4,65,1,54,65,531,556,651,1545,51,5665,561,5156,156,1,56,1,65,64,68,4,35,1,68,78,4,15,4,98,74,51,1,51,984,9889,456,131,58964,86,63,365,48665,153,456,4864,56153,4854,685131365,454,5613,546,4651,31,56465,13,165465,415,11]

#function to check whether the Number is divisible by another number in the list
def check_divisibility(number):
    div_list=[]
    global my_list
    for i in range(len(my_list)):
        if number % my_list[i]==0:
            div_list.append(my_list[i])
    if len(div_list)>0:
        print("The given number is divisible by -")
        print(div_list)
    else:
        print("The given number is not divisible by any numbers in the list")