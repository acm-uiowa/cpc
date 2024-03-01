import time
from segment_tree import SegmentTreeMax
from for_loop import max_for_loop

def main():
    # [0, 1, 2, etc]
    arr = [i for i in range(100000)]
    seg_tree = SegmentTreeMax(arr)

    # Segment Tree method
    start_time = time.time()
    for _ in range(100):
        max_val = seg_tree.query(0, 0, seg_tree.n - 1, 100, 20000)
    end_time = time.time()
    seg_tree_time = end_time - start_time
    print(f"Segment Tree Time: {end_time - start_time} seconds")

    # For Loop method
    start_time = time.time()
    for _ in range(100):
        max_val = max_for_loop(arr, 100, 20000)
    end_time = time.time()
    for_loop_time = end_time - start_time
    print(f"For Loop Time: {end_time - start_time} seconds")

    print(f"Segment Tree is {for_loop_time / seg_tree_time} times faster")

if __name__ == "__main__":
    main()
