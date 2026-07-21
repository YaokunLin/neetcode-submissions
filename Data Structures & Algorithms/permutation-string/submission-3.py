class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Length of the strings
        len1, len2 = len(s1), len(s2)
        
        # Early return if s1 is longer than s2
        if len1 > len2:
            return False

        # Frequency arrays
        s1_count = [0] * 26  # For counting characters in s1
        s2_count = [0] * 26  # For counting characters in the current window of s2

        # Initialize the frequency array for s1 and the first window of s2
        for i in range(len1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # Sliding window to check the rest of s2
        for i in range(len2 - len1):
            # If current window matches the character count of s1, return True
            if s1_count == s2_count:
                return True

            # Move the window right: Remove the left character of the window
            s2_count[ord(s2[i]) - ord('a')] -= 1
            # Add the new character to the window
            s2_count[ord(s2[i + len1]) - ord('a')] += 1

        # Final check for the last window
        return s1_count == s2_count


    

