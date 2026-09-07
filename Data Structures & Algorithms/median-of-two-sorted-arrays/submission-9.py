class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        A,B = nums1, nums2
        if A > B: A,B = B,A

        l,r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            leftA = A[i] if i >= 0 else float("-inf")
            leftB = B[j] if j >= 0 else float("-inf")
            rightA = A[i + 1] if i + 1 < len(A) else float("inf")
            rightB = B[j + 1] if j + 1 < len(B) else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if total % 2:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA,rightB)) / 2
            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1
            