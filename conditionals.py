marks = int(input('Enter your marks: '));

if marks >= 75:
   print("Grade: A")
elif marks >= 65:
   print("Grade: B")
elif marks >= 40:
   print("Grade: C")
else:
   print("Fail")

choice = input("Enter result in grade: ").lower();

match choice:
    case 'grade':
      print("Your results is based on your marks")
    case 'pass':
      if marks >= 40:
        print("You are passed")
      else:
         print("You are failed")
    case _:
      print('Invalid inputs')
      