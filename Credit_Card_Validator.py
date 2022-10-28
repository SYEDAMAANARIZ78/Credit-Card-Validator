card_no = list(input("Enter Card No: "))
odd_sum = 0
even_sum = 0
double_list = []
for (idx, val) in enumerate(card_no):
    if idx % 2 != 0:
        odd_sum += int(val)
    else:
        double = int((val)* 2)
        double_list.append(double)
        
double_string = ""
for x in double_list:
    double_string += str(x)

double_list = list(double_string)

for x in double_list:
    even_sum += int(x)
    
net_sum = odd_sum + even_sum
if net_sum % 10 == 0:
    print('Valid Card....')
else:
    print('Invalid Card!!')
    
