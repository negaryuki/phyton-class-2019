#**List Methods** :octocat::

List methods are as follows:

`##**Methods**
* .append()
* .clear()	
* .copy()	
* .count()	
* .extend()
* .index()	
* .insert()
* .pop()	
* .remove()
* .reverse()
* .sort()`



Syntax       | Description      | Notes
------------ | -------------    | -------------
list.append(item) | The append() method takes a single item and adds it to the end of the list.| 
list.clear() | The clear() method only empties the given list. It doesn't return any value. | The clear() method doesn't take any parameters.
list.copy() | The copy() method returns a shallow copy of the list.| 
list.count(element) | count() method counts how many times an element has occurred in a list and returns it.| The count() method takes a single argument
list.extend(element)| the element is added to the end of list|
list.index(element)|index() method finds the given element in a list and returns its position.|if the same element is present more than once, index() method returns its smallest/first position.
list.insert(index, element)|Return Value from insert()|The insert() method only inserts the element to the list. It doesn't return anything; returns None.
list.pop(index)|removes the item present at that index.|If no parameter is passed, the default index is -1
list.remove(element)|takes a single element as an argument and removes it from the list.|
list.reverse()|Reverses the elements|The reverse() function doesn't take any argument.
list.sort(key=..., reverse=...)|sort() method doesn't return any value. Rather, it changes the original list. |

*IMPORTANT*:

1. By default, sort() doesn't require any extra parameters. However, it has two optional parameters:

 * *reverse* - If true, the sorted list is reversed (or sorted in Descending order)
 * *key* - function that serves as a key for the sort comparison


IMPORTANT POINT: The Difference between .append and . extend is that if you use :
 .append for 2 data, the data will be nested in the list : ['a', [1, 2]]
 .extend for 2 data, then the data will be added just normally to the list : ['a', 1, 2]


Sources: 
 * https://www.w3schools.com/
 * https://www.programiz.com/