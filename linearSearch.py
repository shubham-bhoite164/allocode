#Find max element in an array it has O(N) running time
# a=[10,3,7,14,20,-2,19]
# max=a[0]

# for i in a:
#     if i>max:
#         max=i

# print("The max element is ",max)

#Reverse the array in O(N) running time
# def reverse(a):
#     start_index=0
#     end_index=len(a)-1

#     while start_index<end_index:
#         a[start_index],a[end_index]=a[end_index],a[start_index]
#         start_index +=1

#         end_index -=1

# a=[1,2,3,4,5,6,7]
# reverse(a)
# print(a)

# Check for plaindrome easy way
# def palindrome(s):
#     if s==s[::-1]:
#         return True
#     return False

# s="madam"
# print(palindrome(s))


# Check for palindrome in hard way
# def palindrome(s):
#     s1=s
#     s=list(s)
#     start_index=0
#     end_index=len(s)-1
#     while start_index<end_index:
#         s[start_index],s[end_index]=s[end_index],s[start_index]
#         start_index +=1
#         end_index -=1
        
#     if s1==''.join(s):
#         return True
#     else:
#         return False

# print(palindrome("madam"))

# Interger reversion
# reversed=0
# remainder=0
# n=1234
# while n!=0:
#     remainder=n%10
#     reversed=reversed*10+remainder
#     n=n//10
# print(reversed)


# Anagram
# def is_anagram(str1,str2):
    
#     if len(str1)!=len(str2):
#         return False
# it has O(NlogN) running time complexity
#     str1=sorted(str1)
#     str2=sorted(str2)

#     for i in range(len(str1)):
#         if str1[i]!=str2[i]:
#             return False
        
#     return True

# print(is_anagram(['r','e','s','t','f','u','l'],['f','l','u','s','t','e','r']))

# Find duplicates in an array is the elements in the array is >0 and less than the length of the array

def find_duplicate(nums):

    for i in nums:
        if nums[abs(i)]>=0:
            nums[abs(i)]=-nums[abs(i)]
        else:
            print("Repeation found : %s "%str(abs(i)))

find_duplicate([1, 2, 3, 1, 4,3])
