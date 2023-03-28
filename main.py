def binary_search (list, element):
  middle = 0 
  start = 0
  end = len(list)
  steps = 0

  while(start <= end):
    print('Step', steps, ':', str(list[start:end+1]))

    steps = steps+1
    middle = (start + end) // 2

    if element == list[middle]:
      return middle
    elif element < list[middle]:
      end = middle-1
    else:
      start = middle+1

  return -1

my_list = [-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,300,5000,14000,200000]
target = 5

binary_search(my_list, target)