# Sıralama Algoritmaları Görselleştirici (Python) 🧮📊

Bu proje, Python dili kullanılarak geliştirilen ve `matplotlib` ile `numpy` kütüphaneleri sayesinde klasik sıralama algoritmalarını **animasyonlu olarak görselleştiren** interaktif bir araçtır. Her algoritma, dizideki öğelerin nasıl karşılaştırıldığını ve yer değiştirdiğini adım adım göstererek algoritmaların çalışma prensibini öğrenmek isteyen kullanıcılar için ideal bir ortam sunar.

---

## 📌 Proje Açıklaması

Sıralama algoritmaları, bilgisayar bilimlerinde temel veri yapısı ve algoritma konularının başında gelir. Bu algoritmaların sadece teorik olarak değil, **görsel olarak anlaşılması** da oldukça önemlidir.

Bu proje sayesinde:

- Kullanıcıdan alınan ya da rastgele oluşturulan diziler sıralanabilir.
- 6 farklı sıralama algoritması kullanılarak işlemler animasyonla gösterilir.
- Öğrenciler veya geliştiriciler, her algoritmanın nasıl çalıştığını adım adım izleyebilir.

---

## 🔧 Uygulanan Sıralama Algoritmaları

| Algoritma         | Zaman Karmaşıklığı (En İyi / Ortalama / En Kötü) | Bellek Kullanımı | Kararlı |
|------------------|---------------------------------------------------|------------------|---------|
| Bubble Sort      | O(n) / O(n²) / O(n²)                              | O(1)             | ✔️       |
| Selection Sort   | O(n²) / O(n²) / O(n²)                             | O(1)             | ❌       |
| Insertion Sort   | O(n) / O(n²) / O(n²)                              | O(1)             | ✔️       |
| Merge Sort       | O(n log n) / O(n log n) / O(n log n)              | O(n)             | ✔️       |
| Heap Sort        | O(n log n) / O(n log n) / O(n log n)              | O(1)             | ❌       |
| Radix Sort       | O(nk)                                             | O(n + k)         | ✔️       |

Her algoritma, bir Python **generator** fonksiyonu olarak tanımlanmıştır ve her önemli işlemden (karşılaştırma, yer değiştirme vb.) sonra dizinin son halini üretir.

---

## 🖥️ Kullanılan Teknolojiler

- **Python 3.7+**
- **Matplotlib** — grafik ve animasyonlar için
- **NumPy** — rastgele sayı üretimi ve dizi işlemleri

---

# Sorting Algorithms Visualizer in Python 🧮📊

This project is an interactive and animated sorting algorithm visualizer developed in Python using `matplotlib` and `numpy`. It demonstrates how classic sorting algorithms work by providing real-time visualizations that help learners and developers understand the inner mechanics of each sorting method step-by-step.

---

## 📌 Project Description

Sorting algorithms are fundamental concepts in computer science and software development. While theoretical knowledge is essential, visualizing how each algorithm works internally makes learning much more effective.

This project enables you to:

- Input your own array or use a randomly generated one.
- Select from six different sorting algorithms.
- Watch each algorithm animate the sorting process, highlighting element movements and comparisons.

---

## 🔧 Implemented Sorting Algorithms

The following algorithms have been implemented and animated:

| Algorithm         | Time Complexity (Best / Avg / Worst) | Space Complexity | Stable |
|------------------|--------------------------------------|------------------|--------|
| Bubble Sort      | O(n) / O(n²) / O(n²)                  | O(1)             | ✔️      |
| Selection Sort   | O(n²) / O(n²) / O(n²)                 | O(1)             | ❌      |
| Insertion Sort   | O(n) / O(n²) / O(n²)                  | O(1)             | ✔️      |
| Merge Sort       | O(n log n) / O(n log n) / O(n log n)  | O(n)             | ✔️      |
| Heap Sort        | O(n log n) / O(n log n) / O(n log n)  | O(1)             | ❌      |
| Radix Sort       | O(nk)                                 | O(n + k)         | ✔️      |

Each algorithm is implemented as a Python generator function that yields the current state of the array after every significant operation (e.g., comparison, swap, insertion).

---

## 🚀 How It Works

1. The user is prompted to enter an array of integers separated by commas.
2. Alternatively, a random array is generated using NumPy for demonstration purposes.
3. For each algorithm, `matplotlib.animation` is used to animate the changes in the array.
4. Bar plots dynamically reflect the changes in the list’s state across iterations.

---

## 🖥️ Technologies & Libraries Used

- **Python 3.7+**
- **Matplotlib** — for visualization and animation.
- **NumPy** — for random number generation and efficient array operations.

---



