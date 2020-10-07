mealCost=float(input("Enter the base cost of the meal: "))
tipPercent=int(input("Tip in Percentage: "))
taxPercent=int(input("Tax in Percentage: "))

taxValue=mealCost*taxPercent/100
tipValue=mealCost*tipPercent/100

totalCost=mealCost+taxValue+tipValue

print(round(totalCost))