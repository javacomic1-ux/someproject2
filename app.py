from mypackage.geometry import area_circle, area_rectangle
from mypackage.statistics import average, maximum

print("Circle area:", area_circle(5))
print("Rectangle area:", area_rectangle(4, 6))

numbers = [10, 20, 30, 40]
print("Average:", average(numbers))
print("Maximum:", maximum(numbers))