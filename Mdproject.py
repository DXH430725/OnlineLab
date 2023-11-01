#Getting data
p = input("请输入p(MPa):")
p = float(p)
p = p*1000000
D = input("请输入D(mm):")
D = float(D)
D = D*0.001
d = input("请输入d(mm):")
d = float(d)
d = d*0.001

#Given data
h=D/4
CA=3*0.001
E=1
Eta=1
S=250*1000000

#Cylindrical shell
if(p<0.385*S*E):
    print("fufill the requirements")
else:
    print("Something Wrong!")

ts = (p * D/2)/(S*E - 0.6*p)

#Hemispherical head and Ellipsodal head
if(p<0.665*S*E):
    print("fufill the requirements")
else:
    print("Something Wrong!")

Th1 = (p * D/2)/(2*S*E - 0.2*p)
Th2 = (p * D)/(2*S*E - 0.2*p)

th = max(Th1,  Th2)

#Opening
tn = (p * d/2)/(S*E - 0.6*p)

#convert
Tn = 7.5*tn
Ts = 1.15*ts

#A1
X = 0.5*d + Ts + Tn
A1 = (2*X - d)*(Ts - ts)

#A2
Y = min(2.5*Ts, 2.5*Tn)
A2 = 2*Y*(Tn - tn)

#A3
Z = min(h, 2.5*Ts, 2.5*Tn)
A3 = 2*Z*(Tn - tn)

#A4 and A5
te = min(0.5*Y, 0.5*(X-0.5*d-Tn))
A4 = (2*te)**2
A5 = 2*(X - 0.5*d - Tn - te)*(Y - te)

#Check opening
#correction factor
F = 1
A = d*ts*F
At = A1 + A2 + A3 + A4 + A5
if(A < At):
    print("Reinforcement is acceptable")
else:
    print("Something Wrong!")

print("_____________________________Variables Checking______________________________________________")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# 获取当前作用域内的所有局部变量
local_variables = locals()

# 创建一个新的列表，将变量名和值复制到其中
var_list = [(var_name, var_value) for var_name, var_value in local_variables.items()]

# 遍历新列表并输出变量名和值
for var_name, var_value in var_list:
    print(f"{var_name} = {var_value}")

