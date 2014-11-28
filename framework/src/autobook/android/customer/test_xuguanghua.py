str = 'AbcABcFERGTrkfdsuiof'
str2 = ''
for i in range(0,len(str)):
    if (str[i].islower()):
        str2 += str[i].upper()
    else:
        str2 += str[i].lower()
print str2



str3 = 'ABCDEFGFEDCBA'
j = int (len(str3)/2)
print j
hw = True
for i in range(0,j-1):
    if str3[i] != str3[len(str3)-1-i]:
        hw = False
        break
print hw



list = [10,3,4,56,8,9,12,29]
for j in range(1,len(list)):
    for i in range(0,len(list)-1):
     if list[i] < list[i+1]:
        t = list[i+1]
        list[i+1] = list[i]
        list[i] = t
        i=i+1
    j=j+1
print list



str4 = 'AieuiwyuirejFdhgdskjfDGTUOIUvklfdhdjkghjk'
str5 = ''
for i in range(0,len(str4)-1):
     if str4[i] in str5 :
        print i
     else:
        str5 += str4[i]
print str5,len(str5)
print str4,len(str4)





























