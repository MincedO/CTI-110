#Brandon, Andrew, Aaron - NUT TAP       
#11/21/23
#

def inch_cm(inches):
    cm = inches * 2.54
    print( inches, 'inches can be converted into ', cm,' centimeters')
    return cm 
        
def cm_meter(cm):
    meter = cm / 100
    print(cm, 'centimeters can be converted into ', meter,' meters')
    return meter

def main():
        inches = input("Enter a value in inches: ")
        while str(inches) != "End":
            cm = inch_cm(float(inches))
            meter = cm_meter(float(cm))
            inches = input("Enter a value in inches: ")
if __name__ == "__main__":
    main()
