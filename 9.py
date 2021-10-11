def odd_numbers(n):
   mult = 1
   while n > 0:
      digit = n % 10 
      if digit % 2 != 0:
            mult = mult * digit
      n = n // 10
   return(mult)


n = input("Введите число:")
try:
   n = int(n)
except ValueError:
   print("Ошибка")
   exit()
print("Произведение равно:", odd_numbers(n))   
    
   

   
            
     
    
    
    
