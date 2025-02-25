from tkinter import *
from tkinter import ttk
import time
import random

root = Tk()
root.title("Sorting Algorithms Visualizer")
root.maxsize(1400, 900)
root.config(bg="white")

algo_name = StringVar()
algo_list = ['Merge Sort', 'Selection Sort', 'Bubble Sort', 'Insertion Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

arr = []


# This function is used for creating vertical bars according to the value present in the array
def displayArr(arr, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    width_x = canvas_width / (len(arr) + 1)
    ini = 4
    space = 2
    tempArr = [i / max(arr) for i in arr]

    for i in range(len(tempArr)):
        x1 = i * width_x + ini + space
        y1 = canvas_height - tempArr[i] * 390
        x2 = (i + 1) * width_x + ini
        y2 = canvas_height
        canvas.create_rectangle(x1, y1, x2, y2, fill=colorArray[i])

    root.update_idletasks()


# GENERATING ARRAY  (you can change array size and range as you wish)
def createArr():
    global arr

    array_size = 20
    range_begin = 20
    range_end = 150

    arr = [122, 41, 134, 112, 41, 233, 32, 52, 123, 86, 212, 261]
    for i in range(0, array_size):
        random_integer = random.randint(range_begin, range_end)
        arr.append(random_integer)

    displayArr(arr, ["blue" for x in range(len(arr))])


def set_speed():
    slow = 0.7
    medium = 0.05
    fast = 0.0000001

    if speed_comboBox.get() == 'Slow':
        return slow
    elif speed_comboBox.get() == 'Medium':
        return medium
    elif speed_comboBox.get() == "Fast":
        return fast


def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

    return arr


def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)

    return [right[0]] + merge(left, right[1:])


def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = merge(left=arr[start:mid + 1], right=arr[mid + 1:end + 1])
            arr[start:start + len(merged_array)] = merged_array

        size *= 2

    return arr


def merge(arr, begin, mid, end, displayArr):
    p = begin
    q = mid + 1
    tempArray = []

    for i in range(begin, end + 1):
        if p > mid:
            tempArray.append(arr[q])
            q += 1
        elif q > end:
            tempArray.append(arr[p])
            p += 1
        elif arr[p] < arr[q]:
            tempArray.append(arr[p])
            p += 1
        else:
            tempArray.append(arr[q])
            q += 1

    for p in range(len(tempArray)):
        arr[begin] = tempArray[p]
        begin += 1


def merge_sort(arr, begin, end, displayArr, tym):
    if begin < end:
        mid = int((begin + end) / 2)
        merge_sort(arr, begin, mid, displayArr, tym)
        merge_sort(arr, mid + 1, end, displayArr, tym)

        merge(arr, begin, mid, end, displayArr)

        displayArr(arr, ["#71189E" if x >= begin and x < mid else "#A225AD" if x == mid
        else "#F381FC" if x > mid and x <= end else "blue" for x in range(len(arr))])
        time.sleep(tym)

    displayArr(arr, ["blue" for x in range(len(arr))])


# SORTING ALGORITHMS ARE HERE!!
def sort():
    global arr  # Declare arr as a global variable

    tym = set_speed()
    n = len(arr)

    if algo_comboBox.get() == 'Merge Sort':
        merge_sort(arr, 0, len(arr) - 1, displayArr, tym)

    elif algo_comboBox.get() == 'Selection Sort':
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

                    displayArr(arr, ["yellow" if x == i else "red" if x == j + 1 else "blue" for x in range(len(arr))])
                    time.sleep(tym)

        displayArr(arr, ["blue" for x in range(len(arr))])

    elif algo_comboBox.get() == 'Bubble Sort':
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

                    displayArr(arr, ["yellow" if x == j else "red" if x == j + 1 else "blue" for x in range(len(arr))])
                    time.sleep(tym)

        displayArr(arr, ["blue" for x in range(len(arr))])

    elif algo_comboBox.get() == 'Insertion Sort':
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while (j >= 0 and key < arr[j]):
                arr[j + 1] = arr[j]
                j -= 1

                displayArr(arr, ["yellow" if x == j else "red" if x == j + 1 else "blue" for x in range(len(arr))])
                time.sleep(tym)
            arr[j + 1] = key

        displayArr(arr, ["blue" for x in range(len(arr))])


display_window = Frame(root, width=900, height=300, bg="white")
display_window.grid(row=0, column=0, padx=10, pady=5)

lbl1 = Label(display_window, text="Algorithm: ", bg="white")
lbl1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_comboBox = ttk.Combobox(display_window, textvariable=algo_name, values=algo_list)
algo_comboBox.grid(row=0, column=1, padx=5, pady=5)
algo_comboBox.current(0)

lbl2 = Label(display_window, text="Sorting Speed: ", bg="white")
lbl2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_comboBox = ttk.Combobox(display_window, textvariable=speed_name, values=speed_list)
speed_comboBox.grid(row=1, column=1, padx=5, pady=5)
speed_comboBox.current(0)

btn1 = Button(display_window, text="Sort", command=sort, bg="#C4C5BF")
btn1.grid(row=4, column=1, padx=5, pady=5)

btn2 = Button(display_window, text="Create Array", command=createArr, bg="#C4C5BF")
btn2.grid(row=4, column=0, padx=5, pady=5)

canvas = Canvas(root, width=800, height=400, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
