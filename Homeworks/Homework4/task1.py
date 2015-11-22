with open('yazkora.txt', "r") as input_file:
    sentences = input_file.read().split('.')
with open('answer.txt', 'w') as export_file:
    for thing in sentences:
        words = thing.split(' ')
        list_of_words = []
        string = ''
        for word in words:
            if word[len(word)-2:] == 'yo':
                  list_of_words.append(word)
        string = (' '.join(list_of_words))
        export_file.write(string+'\n')

                
            
            
                
            



    
    
