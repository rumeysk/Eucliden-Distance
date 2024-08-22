##iki noktanın oklit mesafesini hesaplayan fonksiyon
def euclidenDistance(x,y):
    oklid = 0
    
    for k in range(len(x)):
        oklid += (x[k]- y[k])*(x[k]- y[k])
    oklid **= (1/2)
    return oklid

points = ([-1,2],[-1,4])
sonuc = euclidenDistance(points[0],points[1])
print(sonuc)