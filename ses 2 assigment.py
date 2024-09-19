print("start")
print("this is a calculator to find your BMI (body mass index)")
BB=float(input("enter your body weight(in KG)= "))
TB=float(input("enter your body height(in meter)= "))
result= BB/TB**2
print(result)
print("after knowing the number of your BMI i will cathegorize you either underweight,overweight, or ideal weight")
print(result)
if result <= 18: print("U NEED TO EAT TF!!!")
elif result <= 25: print("DAMN HOT BODY!!!")
elif result >=26: print("U NEED TO FIX UR DIET!!!")







