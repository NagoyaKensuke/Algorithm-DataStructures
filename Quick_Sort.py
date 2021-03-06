import time
import random

#クイックソート処理
def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr
        
    ref = arr[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right
    
#ランダムな要素のlistを作成    
l = random.sample(range(10000000), k=1000)

print(l)

#速度計測
start = time.time()
l = quick_sort(l)
end = time.time() - start

print(l)
print('処理時間は ' + str(end))
