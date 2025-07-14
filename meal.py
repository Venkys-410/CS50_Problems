def main():
    usrTime = input("What's the time now? ").casefold().strip()

    convtTime = convert(usrTime)

    if 7.00 <= convtTime <= 8.00:
        print("It's Breakfast time")
    elif 12.00 <= convtTime <= 13.00:
        print("It's Lunch time")
    elif 18.00 <= convtTime <= 19.00:
        print("It's Dinner time")

def convert(time):
    #convert 12 hour am format into 24 hour float
    if time.endswith("a.m.") or time.endswith("am") or time.endswith("a.m"):
        cleanTime = time.replace("a.m.","").replace("am","").replace("a.m","").strip()
        h,m = map(int,cleanTime.split(":"))
        if h == 12:
            h = 0
        return h+(m/60)
        #print(h+(m/60))


    #convert 12 hour pm format into 24 hour float
    elif time.endswith("p.m.") or time.endswith("pm") or time.endswith("p.m"):
        cleanTime =  time.replace("p.m.","").replace("pm","").replace("p.m","").strip()
        h,m = map(int,cleanTime.split(":"))
        if h != 12:
            h += 12
        return h+(m/60)
    #convert 24 hour format into float
    h,m =  map(int,time.split(":"))
    return h+(m/60)


main()