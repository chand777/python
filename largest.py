largest =None
print('Before:', largest)
for i in [3,41,12,9,74,15]:
  if largest is None:
    largest = i
  if i > largest:
    largest = i
print('largest',largest)