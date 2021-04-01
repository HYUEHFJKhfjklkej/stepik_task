# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

# f(x)= \begin{cases}   1 - (x + 2)^2,\quad &\text{при } x\le -2\\  -\frac x2 ,\quad &\text{при } -2 \lt x \le 2\\   (x-2)^2 + 1,\quad &\text{при } 2 \lt x \end{cases}
# f(x)= 
# ⎩
# ⎨
# ⎧
# ​	
  
#  1−(x+2) 
# 2
#  ,
#  − 
# 2
# x
# ​	
#  ,
#  (x−2) 
# 2
#  +1,
# ​	
  
# при x≤−2
# при −2<x≤2
# при 2<x
# ​	
 
# Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.

def f(x):
    if x<=-2:
        i = (1-(x+2)**2)
        return(i)
    elif x>-2 and x<=2:
        i = -x/2
        return(i)
    elif x>2:
        i = (x-2)**2 + 1
        return(i)
        