# myQueue=[]
# def enqueue(lst: list,element)->list:
#     lst.append(element)
#     return element
# def dequeue(lst: list):
#     if len(lst)>0: return lst.pop(0)
#     elif len(lst)==0:
#         print('\nEmpty queue Cannot dequeue')
#         return
# def is_empty(lst: list)->bool:
#     return len(lst)==0
# def size(lst: list)->int:
#     return len(lst)

# print(is_empty(myQueue))
# print(size(myQueue))
# dequeue(myQueue)

# enqueue(myQueue,1)
# enqueue(myQueue,2)
# enqueue(myQueue,3)
# enqueue(myQueue,4)
# enqueue(myQueue,5)
# enqueue(myQueue,6)
# enqueue(myQueue,7)
# print(myQueue)

# #removing first
# print(f'\nRemoving element {dequeue(myQueue)} from myQueue')
# print(myQueue)

# print('\n',is_empty(myQueue))
# print(size(myQueue))

# print(f'\nRemoving element {dequeue(myQueue)} from myQueue')
# print(myQueue)

# print(f'\nRemoving element {dequeue(myQueue)} from myQueue')
# print(myQueue)

# list_1 = list()
# maximum = 5

# def isEmpty():
#     return len(list_1) == 0 



# def isFull():
#     return len(list_1) == maximum

# def enqueue(element):
#     if not isFull():
#         list_1.insert(0,element)
#         return list_1
#     else:
#         return 'list is already full'


# def dequeue():
#     if not isEmpty():
#         list_1.pop()
#         return list_1

#     else:
#         return 'yo the list is already empty'

# def display(f):
#     print(f)

# display(enqueue(6))
# display(enqueue(7))
# display(enqueue(8))
# display(enqueue(9))
# display(enqueue(10))
# display(isFull())
# display(enqueue(1))

class Queue:
    def __init__(self):
        self.queue = list()

    # check if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # add an element to the queue
    def enqueue(self, data):
        # insert method to add element
        self.queue.insert(0, data)
        # [2, 8, 5, 4]
        return True

    # remove an element from the queue
    def dequeue(self):
        if self.isEmpty():
            return ("Queue is empty!")
        return self.queue.pop()

    # get the size of the queue
    def size(self):
        return len(self.queue)

    # display the queue
    def display(self):
        return self.queue

# create a Queue object
q = Queue()

# insert elements to the queue
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)

# display the queue
print(q.display())

# remove an element from the queue
print(q.dequeue())

# display the queue
print(q.display())

# check the size of the queue
print(q.size())

# check if the queue is empty
print(q.isEmpty())


class AnotherQueue:
    def __init__(self):
        self.queue = list()

    # [1, 2, 3, 4, 5, 6]

    # check if empty
    def isEmpty(self):
        return len(self.queue) == 0

    # enqueue
    def enqueue(self, data):
        self.queue.append(data)

    # dequeue
    def dequeue(self):
        if self.isEmpty():
            return "Queu is empty"

        return self.queue.pop(0)

    def display(self):
        return self.queue



s = AnotherQueue()
print(s.dequeue())
s.enqueue('data')
s.enqueue('another data')
print(s.display())
print(s.dequeue())
print(s.display())
