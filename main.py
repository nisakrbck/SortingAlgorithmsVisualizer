import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Görselleştirme için genel fonksiyon
def visualize_sorting(array, generator, title):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(array)), array, color="skyblue")
    ax.set_title(title)

    def update(array):
        for bar, height in zip(bars, array):
            bar.set_height(height)

    ani = animation.FuncAnimation(fig, func=update, frames=generator, interval=500, repeat=False)
    plt.show()

def bubble_sort(array):   # kabarcık sıralama
    arr = array.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr

def selection_sort(array):  #  her adımda en küçük elemanı seçip sıralanmamış kısmın başına yerleştirir
    arr = array.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

def insertion_sort(array): # Ekleme sıralaması
    arr = array.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1   #  Sıralı kısmın son elemanını işaretler.
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr

def merge_sort(array):  # böl ve fethet yaklaşı
    arr = array.copy()

    def merge_sort_rec(arr, l, r):  # Dizi ikiye bölünür
        if l < r:
            m = (l + r) // 2

            yield from merge_sort_rec(arr, l, m)
            yield from merge_sort_rec(arr, m + 1, r)
            yield from merge(arr, l, m, r)

    def merge(arr, l, m, r):   # Bölünen parçalar sıralanır ve birleştirilir
        left = arr[l:m + 1]
        right = arr[m + 1:r + 1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            yield arr.copy()
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            yield arr.copy()
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            yield arr.copy()

    yield from merge_sort_rec(arr, 0, len(arr) - 1)

def heap_sort(array):
    arr = array.copy()
    n = len(arr)

    def heapify(n, i):  #  bir alt ağacı max-heap yapısına dönüştürmek için kullanılır.
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    # Max-Heap Oluşturma Döngüsü
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
        yield arr
    # Sıralama Döngüsü
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(i, 0)
        yield arr

def radix_sort(array):   # basamağa göre sıraalama:
    arr = array.copy()
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        count = [0] * 10   # Basamak değerlerini  saymak için kullanılan bir dizi
        output = [0] * len(arr)   # sıralama işleminin sonucunu  tutan bir dizi

        # Basamak Değerlerinin Sayılması
        for num in arr:
            count[(num // exp) % 10] += 1

        # Kümülatif Sayma
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Elemanları Doğru Pozisyona Yerleştirme
        for i in range(len(arr) - 1, -1, -1):
            idx = (arr[i] // exp) % 10
            output[count[idx] - 1] = arr[i]
            count[idx] -= 1

        # Diziyi Güncelleme
        for i in range(len(arr)):
            arr[i] = output[i]

        exp *= 10
        yield arr


user_input = input("Diziyi virgülle ayrılmış şekilde giriniz : ")
array_from_user = [int(x) for x in user_input.split(',')]


array_random = np.random.randint(1, 100, 8)
print(f"Rastgele oluşturulan dizi: {array_random}")

# Görselleştirme  (Kullanıcı)
visualize_sorting(array_from_user, bubble_sort(array_from_user), "Bubble Sort (Kullanıcı Input)")
visualize_sorting(array_from_user, selection_sort(array_from_user), "Selection Sort (Kullanıcı Input)")
visualize_sorting(array_from_user, insertion_sort(array_from_user), "Insertion Sort (Kullanıcı Input)")
visualize_sorting(array_from_user, merge_sort(array_from_user), "Merge Sort (Kullanıcı Input)")
visualize_sorting(array_from_user, heap_sort(array_from_user), "Heap Sort (Kullanıcı Input)")
visualize_sorting(array_from_user, radix_sort(array_from_user), "Radix Sort (Kullanıcı Input)")

# Görselleştirme  (Random)
visualize_sorting(array_random, bubble_sort(array_random), "Bubble Sort (Random)")
visualize_sorting(array_random, selection_sort(array_random), "Selection Sort (Random)")
visualize_sorting(array_random, insertion_sort(array_random), "Insertion Sort (Random)")
visualize_sorting(array_random, merge_sort(array_random), "Merge Sort (Random)")
visualize_sorting(array_random, heap_sort(array_random), "Heap Sort (Random)")
visualize_sorting(array_random, radix_sort(array_random), "Radix Sort (Random)")