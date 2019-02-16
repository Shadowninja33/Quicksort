# Quick Sort, Preston Cobb


import time, sys, textwrap


def partition(list, low, high):
    """takes a list, lowindex and high index, and returns a list
    with the pivot (original first element) in their sorted position"""
    pivot = list[low]  #pivot, first element
    left = low + 1     #left-most index after pivot
    right = high        #right-most index after pivot
    sorted = False

    while not sorted:
        #loop until a large number is found on the left, or left = right
        while left <= right and list[left] <= pivot:
            left += 1

        #loop until a small number if found on the right, or right = left
        while right >= left and list[right] > pivot:
            right -=1

        if right < left:
            sorted = True
        else:
            #swap the two elements
            list[left], list[right] = list[right], list[left]

    #swapping the pivot and the rightcounter, putting it in its correct position
    list[low], list[right] = list[right], list[low]

    return right


def quicksort(list, low, high):
    """Recurvily calls the quicksort alg on the unsorted
    parts of the array"""
    if(low < high):
        partitionindex = partition(list, low, high)

        quicksort(list, low, partitionindex-1)
        quicksort(list, partitionindex + 1, high)


if __name__ == "__main__":

    filelen = int(sys.argv[1])
    inputfile = sys.argv[2]

    #reads in the specified file and splits it into a list
    with open(inputfile) as f:
        numbers = f.read().split()

    #convert the input string list to a list of ints to be sorted
    numbers = list(map(int, numbers))

    starttime = time.time()
    quicksort(numbers, 0, len(numbers) - 1)

    print("%.3f" % ((time.time() - starttime) * 1000))

    finalnums = ' '.join(map(str, numbers))

    with open("output.txt", mode='w') as fwrite:
        fwrite.write(textwrap.fill(finalnums, width=20))



