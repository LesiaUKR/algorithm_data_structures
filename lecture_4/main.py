import timeit
import random

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quicksort_recursion
from radix_sort import radix_sort
from selection_sort import selection_sort
from shell_sort import shell_sort


if __name__ == "__main__":
   data_small = [random.randint(0, 1_000) for _ in range(100)]
   data_medium = [random.randint(0, 10_000) for _ in range(1_000)]
   data_large = [random.randint(0, 100_000) for _ in range(10_000)]
   
   ts_bubble = timeit.timeit(lambda: bubble_sort(data_small), number=1)
   ts_insertion = timeit.timeit(lambda: insertion_sort(data_small), number=1)
   ts_merge = timeit.timeit(lambda: merge_sort(data_small), number=1)
   ts_quick = timeit.timeit(lambda: quicksort_recursion(data_small), number=1)
   ts_radix = timeit.timeit(lambda: radix_sort(data_small), number=1)
   ts_selection = timeit.timeit(lambda: selection_sort(data_small), number=1)
   ts_shell = timeit.timeit(lambda: shell_sort(data_small), number=1)
   ts_timsorted = timeit.timeit(lambda: sorted(data_small[:]), number=1)
   ts_timsort = timeit.timeit(lambda: data_small[:].sort(), number=1)

   tm_bubble = timeit.timeit(lambda: bubble_sort(data_medium), number=1)
   tm_insertion = timeit.timeit(lambda: insertion_sort(data_medium), number=1)
   tm_merge = timeit.timeit(lambda: merge_sort(data_medium), number=1)
   tm_radix = timeit.timeit(lambda: radix_sort(data_medium), number=1)
   tm_quick = timeit.timeit(lambda: quicksort_recursion(data_medium), number=1)
   tm_selection = timeit.timeit(lambda: selection_sort(data_medium), number=1)
   tm_shell = timeit.timeit(lambda: shell_sort(data_medium), number=1)
   tm_timsorted = timeit.timeit(lambda: sorted(data_medium[:]), number=1)
   tm_timsort = timeit.timeit(lambda: data_medium[:].sort(), number=1)

   tl_bubble = timeit.timeit(lambda: bubble_sort(data_large), number=1)
   tl_insertion = timeit.timeit(lambda: insertion_sort(data_large), number=1)
   tl_merge = timeit.timeit(lambda: merge_sort(data_large), number=1)
   tl_radix = timeit.timeit(lambda: radix_sort(data_large), number=1)
   tl_quick = timeit.timeit(lambda: quicksort_recursion(data_large), number=1)
   tl_selection = timeit.timeit(lambda: selection_sort(data_large), number=1)
   tl_shell = timeit.timeit(lambda: shell_sort(data_large), number=1)
   tl_timsorted = timeit.timeit(lambda: sorted(data_large[:]), number=1)
   tl_timsort = timeit.timeit(lambda: data_large[:].sort(), number=1)

   print(f"| {'Algorithm':<20} | {'Small':<20} | {'Medium':<20} | {'Large':<20} |")
   print(f"| {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} |")
   print(f"| {'Bubble Sort':<20} | {ts_bubble:20.5f} | {tm_bubble:20.5f} | {tl_bubble:20.5f} |")
   print(f"| {'Insertion Sort':<20} | {ts_insertion:20.5f} | {tm_insertion:20.5f} | {tl_insertion:20.5f} |")
   print(f"| {'Merge Sort':<20} | {ts_merge:20.5f} | {tm_merge:20.5f} | {tl_merge:20.5f} |")
   print(f"| {'Quick Sort':<20} | {ts_quick:20.5f} | {tm_quick:20.5f} | {tl_quick:20.5f} |")
   print(f"| {'Radix Sort':<20} | {ts_radix:20.5f} | {tm_radix:20.5f} | {tl_radix:20.5f} |")
   print(f"| {'Selection Sort':<20} | {ts_selection:20.5f} | {tm_selection:20.5f} | {tl_selection:20.5f} |")
   print(f"| {'Shell Sort':<20} | {ts_shell:20.5f} | {tm_shell:20.5f} | {tl_shell:20.5f} |")
   print(f"| {'Timsort (sorted)':<20} | {ts_timsorted:20.5f} | {tm_timsorted:20.5f} | {tl_timsorted:20.5f} |")
   print(f"| {'Timsort (sort)':<20} | {ts_timsort:20.5f} | {tm_timsort:20.5f} | {tl_timsort:20.5f} |")

   
