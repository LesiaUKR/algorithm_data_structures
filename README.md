# Basic Algorithm and Data Structures

### Lecture_4 Compare sorting algorithms

| Algorithm            | Small                | Medium               | Large                |
| --------------------: | :--------------------: | :--------------------: | :--------------------: |
| Bubble Sort          |              0.00085 |              0.10026 |             10.65921 |
| Insertion Sort       |              0.00042 |              0.03236 |              4.52997 |
| Merge Sort           |              0.00036 |              0.00319 |              0.04996 |
| Quick Sort           |              0.00018 |              0.00228 |              0.03313 |
| Radix Sort           |              0.00015 |              0.00194 |              0.02909 |
| Selection Sort       |              0.00030 |              0.04345 |              4.17431 |
| Shell Sort           |              0.00011 |              0.00247 |              0.04840 |
| Timsort (sorted)     |              0.00001 |              0.00003 |              0.00021 |
| Timsort (sort)       |              0.00000 |              0.00001 |              0.00015 |


## Assignment Description

Python has two built-in sorting functions: sorted and sort. Python's sorting functions use Timsort, a hybrid sorting algorithm that combines merge sort and insertion sort.

Compare three sorting algorithms: merge sort, insertion sort, and Timsort, based on their execution time. Your analysis should be supported by empirical data obtained through testing these algorithms on various datasets. Empirically verify the theoretical complexity estimates of the algorithms, particularly by sorting large arrays. Use the timeit module to measure the execution time of the algorithms.

Demonstrate that the combination of merge sort and insertion sort makes Timsort significantly more efficient. This explains why programmers generally prefer using Python's built-in algorithms rather than implementing their own. Draw conclusions based on the efficiency findings of the algorithms for this specific case.

Assignment involves comparing three sorting algorithms: Merge Sort, Insertion Sort, and Timsort, specifically focusing on their empirical performance across different datasets.

Here's a breakdown of the tasks:

1. **Algorithm Comparison**: Compare the performance (execution time) of Merge Sort, Insertion Sort, and Timsort.

2. **Empirical Data**: Gather empirical data through testing these algorithms on various datasets to validate theoretical complexity estimates, especially on large arrays.

3. **Time Measurement**: Utilize Python's timeit module to accurately measure the execution time of each sorting algorithm.

4. **Analysis**: Demonstrate that the hybrid nature of Timsort (combining Merge Sort and Insertion Sort) significantly enhances its efficiency. This explains why programmers often prefer using built-in Python sorting algorithms rather than implementing their own.

5. **Conclusion**: Draw conclusions based on your empirical findings regarding the effectiveness and practicality of Timsort compared to Merge Sort and Insertion Sort in readme.md file.

# Висновки щодо результатів тестування алгоритмів
