# Arrays

### Time Complexity
| Algorithm | Average Case | Worst Case |
|-----------|--------------|------------|
| Access    | O(1)         | O(1)       |
| Search    | O(n)         | O(n)       |
| Insertion | O(n)         | O(n)       |
| Deletion  | O(n)         | O(n)       |

### Types of Arrays
- Static:
    - Size is fixed at compile time 
    - Elements can be modified, but memory allocation cannot
- Dynamic
  - Size can change
  - Elements can be added at runtime

### Pros
Arrays are excellent for fast searches. O(1)

Elements exist in contiguous memory locations 
which speeds up processing. (Ordered)

Pushing and popping elements to the end of the array is
extremely fast. O(1)

### Cons 
Slow insertions/deletions if not at end. O(n)

Can cause issues if a static array exceeds its memory 
allocation

## Arrays in Python
Python arrays are dynamic lists. They are ordered, mutable, allow 
duplicates and can contain any data type. A list can also contain multiple
distinct data types.

### Built-in Methods
```python
#Instantiate
mylist = ['a', 'b', 'c']
mylist = list(('a', 'b', 'c'))

#Add elements
mylist.append(e) #Pushes e to end of list
mylist.extend(list2) #Appends elements of list2 to mylist
mylist.insert(i, e) #inserts element e and index i
mylist + list2 #Concatenates two lists
mylist * x #Extends list onto itself (x-1) times

#Remove Elements
mylist.clear() #Deletes all elements
mylist.remove(x) #Removes first instance of an element with value x
mylist.pop(i=-1) #Removes element at index i -> e

#Other
len(mylist) #-> number of elements in list
mylist.copy() #-> shallow copy
mylist.deepcopy() #-> deep copy
mylist.count(x) #-> number of elements with value == x
mylist.index(x) #-> index of first element with value == x
mylist.reverse() #Reverses list in place -> None
sorted(mylist) #Creates a new sorted list with the elements of mylist
mylist.sort() #Compares elements with "<" operator and sorts in ascending order -> None
mylist.sort(key = <, reverse = False) # KEYWORD ONLY. If reverse = True, 
#the list will sort in descending order. A function can be assigned as
#the key for custom sorting.
min(mylist)/max(mylist) #-> returns min or max value. Must be homogenous
mylist[i=1:j=-1:k=1] #Returns a slice of the list from i to j in steps of k
#[::-1] will return the list in reverse.

# Get First and Last element of a list
mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
first, *x, last = mList
print(first) #63
print(last) #10



