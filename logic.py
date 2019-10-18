A = False 
B = False 
C = False 
def log_func (x,y,z): 
    tmp1 = x or (y and z) 
    tmp2 = (x or y) and (x or z) 
    return str(int((not(tmp1)or tmp2)and(tmp1 or not(tmp2)))) 
def log_func2 (x,z): 
    tmp1 = not(x or not(z) and x) 
    tmp3 = not(x) and z 
    tmp2 = not(not(tmp3)or z) 
    return str(int((not (tmp1) or tmp2) and (tmp1 or not (tmp2)))) 
print(chr(172) + chr(741) + chr(745) + chr(866) + chr(709) + chr(708) + chr(8660)) 
print("-"*53) 
print("| A | B | C |" + " A"+chr(709)+"(B"+chr(708)+"C)" + 
chr(8660)+"(A"+chr(709)+"B)"+chr(708)+ "(A"+chr(709)+"C) |") 
print("-"*53) 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
print("-"*53) 
C = True 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,(C)) + " "*12 + "|") 
print("-"*53) 
B = True 
C = False 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
B = True 
C = True 
print("-"*53)    
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
A = True 
B = False 
C = False 
print("-"*53) 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
C = True 
print("-"*53) 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
B = True 
C = False 
print("-"*53) 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
C = True 
print("-"*53) 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
print("-"*53) 
print(""*53) 
print(" "*53) 
print("-"*44) 
A = False 
C = False 
print("| A | C |" + " " + chr(172) +"(A" +chr(709)+chr(172)+"C"+chr(708)+ "A)" 
+ chr(8660)+ chr(172)+"("+chr(172)+ "A"+chr(708)+"C"+chr(8594)+"C ) |") 
print("-"*44)
print("| "+ str(int(A)) + " | " + str(int(C)) + " | " + log_func2(A,C) + " |") 
print("-"*44) 
C = True 
print("| "+ str(int(A)) + " | " + str(int(C)) + " | " + log_func2(A,C) + " |") 
print("-"*44) 
A = True 
C = False 
print("| "+ str(int(A)) + " | " + str(int(C)) + " | " + log_func2(A,C) + " |") 
print("-"*44) 
C = True 
print("| "+ str(int(A)) + " | " + str(int(C)) + " | " + log_func2(A,C) + " |") 
print("-"*44)
