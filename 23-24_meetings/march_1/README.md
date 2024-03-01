# Segment Trees

## Problem Statement
Given an array of integers, you need to find the maximum value in different subarrays multiple times.

## Solutions
<details>


### 1. For Loop
<details>

  <summary>Click to expand</summary>
  
  **Approach:** Iterate through the specified subarray and find the maximum value.

  - **Time Complexity:** O(n) for each query, where n is the size of the subarray.
  - **Space Complexity:** O(1), as no extra space is required.
</details>

<details>


### 2. NxN Matrix
<details>
  <summary>Click to expand</summary>
  
  **Approach:** Create an nxn matrix where each cell (i, j) stores the maximum value in the subarray from index i to j.

  - **Time Complexity:** 
    - Building the matrix: O(n^2), where n is the size of the array.
    - Querying for the maximum: O(1) for each query.
  - **Space Complexity:** O(n^2), as the matrix requires additional space proportional to the square of the size of the array.
</details>

<details>

### 3. Segment Tree
<details>
  <summary>Click to expand</summary>
  
  **Approach:** Build a segment tree from the array, and use it to efficiently find the maximum value in a given range.

  - **Time Complexity:** 
    - Building the tree: O(n), where n is the size of the array.
    - Querying for the maximum: O(log n) for each query.
  - **Space Complexity:** O(n), as the segment tree requires additional space proportional to the size of the array.
</details>
</details>
</details>

</details>
