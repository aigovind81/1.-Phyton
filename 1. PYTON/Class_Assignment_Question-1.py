class SubfieldsInAI:
    @staticmethod
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")

SubfieldsInAI.Subfields()

class OddEven:
    def OddEven():
        num = int(input("Enter a number: "))
        
        if num % 2 == 0:
            print(f"{num} is Even number")
        else:
            print(f"{num} is Odd number")

OddEven.OddEven()


class Elegibilityformarriage:
    def Elegibilityformarriage():
        gender = input("Your Gender:")
        age = int(input("Your Age:"))
        
        if age > 21:
            print("Eligibility for Marriage")
        else:
            print("NOT Eligibility for Marriage")  

Elegibilityformarriage.Elegibilityformarriage()

class FindPercent:
    @staticmethod
    def percentage():
        subject1 = int(input("Enter Subject 1 marks:"))
        subject2 = int(input("Enter Subject 2 marks:"))
        subject3 = int(input("Enter Subject 3 marks:"))
        subject4 = int(input("Enter Subject 4 marks:"))
        subject5 = int(input("Enter Subject 5 marks:"))
        
        total = subject1 + subject2 + subject3 + subject4 + subject5
        percentage = (total / 500) * 100
        
        print(f"\nSubject1= {subject1}")
        print(f"Subject2= {subject2}")
        print(f"Subject3= {subject3}")
        print(f"Subject4= {subject4}")
        print(f"Subject5= {subject5}")
        print(f"Total : {total}")
        print(f"Percentage : {round(percentage, 2)}%")

FindPercent.percentage()

class triangle:
    @staticmethod
    def triangle():
        Height=32
        Breadth=34 
        Area=(Height*Breadth)/2
        
        print(f"Height:{Height}")
        print(f"Breadth:{Breadth}")
        print(f"Area of Formula:(Height*Breadth)/2")
        print(f"Area of Triangle:{Area}")

        height1=2
        height2=4
        breadth=4
        Area1=(height1 + height2 + breadth)

        print(f"Height1:{height1}")
        print(f"Height2:{height2}")
        print(f"Breadth:{breadth}")
        print(f"Permiter formula: Height1+Height2+Breadth")
        print(f"Permiter of Triangle: {Area1}")

triangle.triangle()