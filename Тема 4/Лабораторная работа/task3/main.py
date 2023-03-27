def delete(list_, index=None):
 # TODO реализовать функцию удаления элемента из списка по индексу
 #    list_.pop(index) if index is not None else list_.pop() #вариант проще
 if index is None:
     list_.pop()
     return list_
 else:
     l1 = list_[:index]
     l2 = list_[index:]
     l2.pop(0)
     l1.extend(l2)
 return l1


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
