###############################################################
# This is a min heapsort code (Problem 5A). Here,
# I define several functions such as insertion, extract_min, is_empty, heapsort.
# Author: Nusrat Sarmin
# Date: 11/26/2018
##############################################################
class Heap:

    def __init__(self):
        self.heap_array = []

    def insert(self, elem):
        self.heap_array.append(elem)

        i = len(self.heap_array) - 1
        while i > 0:
            # If element inserted is less than its parent, swap
            if self.heap_array[i] < self.heap_array[(i-1)//2]:
                temp = self.heap_array[i]
                self.heap_array[i] = self.heap_array[(i-1)//2]
                self.heap_array[(i-1)//2] = temp
                i = (i-1)//2
            else:
                break

    # This function extracts the min element from a heap and
    # ensures the heap properties are preserved
    def extract_min_value(self):
        if self.is_empty():
            return None

        min_value = self.heap_array[0]
        new_first = self.heap_array.pop()
        if len(self.heap_array) > 0:
            # Make the last element of the list the head
            self.heap_array[0] = new_first
            num = 0
            while i < len(self.heap_array):
                cur_index = 2*num +1
                x_index = 2*num +2
                min_index = num
                # check left and right children of current node (if they exist)
                while cur_index < len(self.heap_array) and cur_index <= x_index:
                    # If the current min value is greater than the child,
                    # then make the index of the child.
                    if self.heap_array[min_index] > self.heap_array[cur_index]:
                        min_index = cur_index
                    cur_index += 1
                # If all three values are the same then no need to swap
                if num == min_index:
                    break
                # else, swap the current node with the min
                temp = self.heap_array[num]
                self.heap_array[num] = self.heap_array[min_index]
                self.heap_array[min_index] = temp

                # swapping if needed
                num = min_index

        # Return the min element
        return min_value

    def is_empty(self):
        return len(self.heap_array) == 0

# This function receives a min-heap and returns a sorted array
def heapsort(heap):
    result = []
    for i in range(len(heap.heap_array)):
        result.append(heap.extract_min())
    return result

# This function creates heap and returns a heap
def create_heap(filename):
    file = open(filename, "r")
    heap = Heap()
    numbers = file.readline().split(",")
    for number in numbers:
        heap.insert(int(number))
    return heap


# Function that allows user to provide file to test the heapsort function.
def main():
    while True:
        try:
            filename = input("Enter the path to the txt file that contains the numbers separated by commas (press RETURN for default file or \"q\" to quit):\n")
            # If user pressed RETURN, use default file
            if filename == "":
                filename = "numbers.txt"
            elif filename.lower() == "n":
                return
            # Create heap with specified or default file
            heap = create_heap(filename)
            # Sort array using heapsort
            sorted = heapsort(heap)
            print("Sorted array:")
            # Print the sorted array, 40 numbers per line maximum
            for num in range(len(sorted)):
                if num % 40 == 0:
                    print()
                print(str(sorted[num]), end="")
                if num != len(sorted)-1:
                    print(", ", end="")
            print()
            return
        except FileNotFoundError:
            print("File not found. Try again.")
        except ValueError:
            print("Error: Please verify that the file contains only integers separated by commas.")
        except Exception as Ex:
            print(Ex)

main()
