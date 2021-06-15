import array as arr

cols = 4

def Sum(a, b):
    print(len(a))
    rows = len(a)
    count = 0
    counts = 0

    sumG = [[0 for i in range(cols)] for j in range(rows)]

    for i in range (len(a)):
        sumG[i][0]=a[i][0]
        sumG[i][1]=a[i][1]
        sumG[i][2]=a[i][2]
        sumG[i][3]=a[i][3]

    rows1 = len(b)
    print(len(b))

    sumR = [[0 for i in range(cols)] for j in range(rows1)]

    for i in range (len(b)):
        sumR[i][0] = b[i][0]
        sumR[i][1] = b[i][1]
        sumR[i][2] = b[i][2]
        sumR[i][3] = b[i][3]

    for i in range (len(a)):
        for y in range (len(b)):
            if sumG[i][0] == sumR[y][0]:
                count +=1
    
    sum = [[0 for i in range(cols)] for j in range(rows)]
    
    for i in range (len(a)):
        for y in range (len(b)):
            if sumG[i][0] == sumR[y][0]:
                sum[i][0] = sumG[i][0]
                sum[i][1] = float(sumG[i][1]) + float(sumR[y][1])
                sum[i][1] = round(sum[i][1], 4)
                sum[i][1] = sum[i][1] * 100
                sum[i][2] = sumG[i][2]
                sum[i][3] = sumG[i][3]

    for i in range (len(a)):
        if sum[i][0] == 0:
            counts +=1
            
    print(counts)

    for i in range (len(a)):
        if sum[i][0] == 0:
            sum[i][0] = sumG[i][0]
            sum[i][1] = float(sumG[i][1])
            sum[i][1] = round(sum[i][1], 4)
            sum[i][1] = sum[i][1] * 100
            sum[i][2] = sumG[i][2]
            sum[i][3] = sumG[i][3]

    #print(sum)
        
    return sum