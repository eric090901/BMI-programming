height = input('input height: ')
weight = input('input weight: ')
height = float(height)
weight = float(weight)
BMI = weight / (height * height)
BMI = float(BMI)
if BMI < 18.5 :
   print('too thin')
elif BMI >= 18.5 and BMI < 24.0 :
   print('normal')
elif BMI >= 24 and BMI < 27.0 : 
   print('overweight')
elif BMI >= 27 and BMI < 30.0 :
   print('little fat') 
elif BMI >= 30 and BMI < 35.0 :
   print('medium fat')
else : 
   print('too fat')
