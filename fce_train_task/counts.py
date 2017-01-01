import re

fcesheet = open('fce_train.gold.max.rasp.old_cat.m2')

reader = fcesheet.readlines()
sentence_count = 0
no_error_count = 0

for index, line in enumerate(reader):
    if line.startswith('S'):
        sentence_count += 1
        if re.match(r'^[^A]', reader[index + 1]):
            no_error_count += 1


print 'The sentence count is {sentence_count}. The sentences without errors are {no_error_count}.'.format(
      sentence_count=sentence_count, no_error_count=no_error_count)

fcesheet.close()