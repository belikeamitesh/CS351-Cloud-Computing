from typing import List, Dict, Set, Optional
import functools
import random

# Question 1


def splitWord(word: str) -> List[str]:
    """Return the  list of characters formed by breaking the string name.
    doctests:
    >>> splitWord("abc")
    ['a', 'b', 'c']
    >>> splitWord("a")
    ['a']
    """
    charList = list(word)
    return charList


# Question 2


def joinChar(characters: List[str]) -> str:
    """Return the string formed by joining all the characters.
    doctests:
    >>> joinChar(['a','b','c'])
    'abc'
    >>> joinChar(['h','e','l','l','o'])
    'hello'
    """
    string = ""
    return string.join(characters)


# Question 3


def randomnums(n: int) -> List[int]:
    """Returns a list of n random numbers
    doctest:
    >>> random.seed(2)
    >>> randomnums(6)
    [1, 1, 1, 3, 2, 6]

    >>> random.seed(5)
    >>> randomnums(8)
    [5, 6, 1, 8, 4, 1, 3, 2]
    """
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(1, n))
    return rand_list


# Question 4


def sortInDescendingOrder(nums: List[int]) -> List[int]:
    """Returns a list of numbers sorted in decending order.

    doctests:
    >>> sortInDescendingOrder([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]

    >>> sortInDescendingOrder([11, 8, 13, 5, 2])
    [13, 11, 8, 5, 2]

    """
    return sorted(nums, reverse=True)


# Question 5


def getFrequency(nums: List[int]) -> Dict[int, int]:
    """Returns the frequency of each number in the given list.
    doctests:
    >>> getFrequency([1,1,3,2,3,2,3,2,2])
    {1: 2, 3: 3, 2: 4}
    >>> getFrequency([2, 3, 5, 3, 2, 1, 5, 3, 6])
    {2: 2, 3: 3, 5: 2, 1: 1, 6: 1}
    """
    freq = {}
    for num in nums:
        key = num
        value = nums.count(num)
        freq.update({key: value})
    return freq


# Question 6


def getUniqueElements(nums: List[int]) -> Set:
    """Returns the unique element from the given list.

    doctests:
    >>> getUniqueElements([1, 1, 3, 2, 3, 2, 3, 2, 2])
    {1, 2, 3}
    >>> getUniqueElements([1, 4, 4, 2, 3, 3, 2, 1, 6])
    {1, 2, 3, 4, 6}
    """
    return set(nums)


# Question 7


def firstRepeatingElement(nums: List[int]) -> Optional[int]:
    """Returns the first repeated element in the list

    doctests:
    >>> firstRepeatingElement([1,2,3,3,5,1,2])
    3
    >>> firstRepeatingElement([2,1,2,3,1])
    2
    """
    st: Set[int] = set()
    for num in nums:
        if num in st:
            return num
        st.add(num)
    return None


# Question 8


def SquaresandCubes(n: int) -> Dict[int, List[int]]:
    """Returns the square and cube of number from 0 to n

    doctests:
    >>> SquaresandCubes(6)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27], 4: [16, 64], 5: [25, 125], 6: [36, 216]}
    """
    result = {}
    for i in range(n + 1):
        result[i] = [i * i, i * i * i]
    return result


# Question 9


def tupleSameIndex(nums1: List, nums2: List) -> List:
    """Returns tuples of each consecutive element having same index

    doctests:
    >>> tupleSameIndex([1,2,3,4], ['a','b','c','d'])
    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    """
    return list(zip(nums1, nums2))


# Question 10


def generateSquare(n: int) -> List[int]:
    """Returns a list of squares from 0 to n using list comprehension.
    >>> generateSquare(5)
    [0, 1, 4, 9, 16, 25]
    >>> generateSquare(10)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """
    return [x ** 2 for x in range(n + 1)]


# Question 11


def generateSquareDict(n: int) -> Dict[int, int]:
    """Returns a dictionary mapping squares from 0 to n using dictionary comprehension.
    >>> generateSquareDict(6)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
    >>> generateSquareDict(10)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    """
    return {x: x ** 2 for x in range(n + 1)}


# Question 12


def classList():
    class MyClass:
        def __init__(self, nums: List) -> None:
            self.nums = nums

        def apply(self, func):
            try:
                return list(map(func, self.arr))
            except:
                raise Exception("custom error") from TypeError()

    """
    Applies a function on the saved input list nums and gives an output, and raises a custom error if function is not valid on the list nums

    >>> ans = MyClass([1, 2, 3, 4, 5])
    >>> ans.apply(lambda x:x**3))
    [1, 8, 27, 64, 125]
    
    >>> ans = MyClass([1, 2, 3, 4, 5])
    >>> ans.apply(lambda x:x+5)
    [6, 7, 8, 9, 10]
    
    >>> ans = MyClass(['a','b','c'])
    >>> ans.apply(lambda x:x**2)
    Traceback (most recent call last):
        ...
    Exception: custom error
    """


# Question 13


def upperCase(words: List[str]) -> List[str]:
    """Returns upper-cases of each word in the list words.
    >>> upperCase(['aa','bb','cd','e'])
    ['AA', 'BB', 'CD', 'E']
    """
    return [x.upper() for x in words]


# Question 14


def productAll(nums: List[int]) -> int:
    """Returns product of all numbers in the list nums using functools.reduce in some capacity.
    >>> productAll([1,2,3,4,5])
    120
    >>> productAll([1,2,3])
    6
    """
    return functools.reduce((lambda x, y: x * y), nums)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
