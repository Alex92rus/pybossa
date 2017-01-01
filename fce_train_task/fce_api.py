import re

def extract_data(filename):
    #open file
    fce_file = open(filename)

    #read the lines
    iter_lines = fce_file.readlines()
    
    #array of tuples - (sentence, [error_spans])
    data = []
    
    #packet the error spans with their corresponding sentence
    for line in iter_lines:
        #appending the sentence to the data
        if line[0] == 'S':
            data.append((line[1:-2], []))
        elif line[0] == 'A':
            tokens = line.split(' ')
            start = int(tokens[1])
            error_details = tokens[2].split('|||')
            end = int(error_details[0])
            error_type = error_details[1]
            data[-1][1].append((start, end, error_type))
    
    #close file
    fce_file.close()
    
    return data

if __name__ == '__main__':
    fce_data = extract_data('fce_train.gold.max.rasp.old_cat.m2')
    print("Sentence: {sentence} with list of error indecies {errors}".format(sentence=data[12][0], errors=data[12][1]))