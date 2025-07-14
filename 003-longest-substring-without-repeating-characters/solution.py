class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0  # Left boundary of the sliding window
        max_length = 0  # Stores the length of the longest substring

    # Expand the window using the right pointer
        for right in range(len(s)):
            # If a duplicate character is found, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1  # Move the left pointer forward

            # Add the current character to the set
            char_set.add(s[right])

            # Update max_length with the size of the current window
            max_length = max(max_length, right - left + 1)

        return max_length
        
