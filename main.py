# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(str1, str2):
    # [assignment] Add your code here

   str1_anagrams = sorted(str1)
   str2_anagrams = sorted(str2)

   if(str1_anagrams == str2_anagrams):
       return True
   else:
        return False

print(find_anagrams("listen", "silent"))