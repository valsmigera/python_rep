import time


count = 0   # 1
range_count = 10    # 2
for_count = 0   # 3
run = True  # 4
while run:  # 5
    print('Hello Cycle')    # 5.1
while run:  # 6
    print('Step = ', count)    # 6.1
    count += 1  # 6.2
    time.sleep(0.5)
while count < range_count:      # 7
    print('Step=', count)   # 7.1
    count += 1  # 7.2
while count < range_count:  # 8
    print('Step=', count)   # 8.1
    count += 1  # 8.2
    if count == 3:  # 8.3
        print("Step=", count, "If body")
    else:
        print("Don't working")
while run:  # 9
    print('Step=', count)   # 9.1
    count += 1  # 9.2
    if count == range_count:    # 9.3
        print("Stop", count)    # 9.4
        break
for i in range(for_count, range_count):     # 10
    print("Step =", range_count)    # 10.1
for item in range(30):  # 11
    print("Step=", item)    # 11.1
    if item == 5:   # 11.2
        print("Item =", item)
    elif item == 10:    # 11.3
        print("Item =", item)
    elif item < 4:  # 11.4
        print("Item <", item)
    elif item >= 27:    # 11.5
        print("Item >=", item)
    break
for item in range(0, range_count + 1):  # 12
    print("Step =", item)   # 12.1
    if item == 7:   # 12.2
        inner_count = 0
        print("-- inner_count =", inner_count)
        for inner_item in range(0, item):
            print("-------- Inner_Step =", inner_item)
            if inner_item == 5:
                inner_count == inner_item
            else:
                ("Don't worry")
    else:
        ("-- inner_count =", inner_count)
for item in range(0, 20):   # 13
    print("Step =", item)   # 13.1
    if item > 7 < 12:   # 13.2
        print("If_item =", item)
        continue
    print('End_iteration =', item)  # 13.3