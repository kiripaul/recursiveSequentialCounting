def pushupCounter(maxCount):
    if maxCount == 1:
        return(1)
    else:
        return(maxCount + pushupCounter(maxCount-1))

def Main():
    total = pushupCounter(12)
    print(total)

Main()
