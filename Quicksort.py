def quick_sort(ARRAY):
    ARRAY_MAX = len(ARRAY)
    if( ARRAY_MAX <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        big = [ element for element in ARRAY[1:] if element > PIVOT ]
        small = [ element for element in ARRAY[1:] if element <= PIVOT ]
        return quick_sort(small) + [PIVOT] + quick_sort(big)
    
import sys
if (len(sys.argv) <= 1):
    print("매개변수가 없습니다")

print(sys.argv)


tp = 0
tp2 = []
for i in range(0, len(sys.argv)):
    if sys.argv[i] == '-o':
        tp = sys.argv[i + 1]
    if sys.argv[i] == '-i':
        tp2 = sys.argv[i + 1:]

print(tp)

print(tp2)
tp2 = list(map(int, tp2))

tp2 = quick_sort(tp2)

if tp == 'A':
    print(tp2)
else:
    tp2.reverse()
    print(tp2)