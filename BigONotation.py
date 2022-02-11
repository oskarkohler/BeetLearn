from typing import List, Tuple


def question3(first_list: List[int], second_list: List[int])-> List[int]:
   temp: List[int] = first_list[:]
   for el_second_list in second_list:
      flag = False
      for check in temp:
         if second_list == check:
            flag = True
            break
      if not flag:
         temp.append(el_second_list)
   return temp

print(question3([1,2,3],[1,2,3]))