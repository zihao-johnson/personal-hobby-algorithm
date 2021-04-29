from string_sort import insert_sort

def remove(string, list_string):

    '''
        binary search to find the target string-seq, taking O(m*log(n)) time complexity 
        where m is the length of seq to be removed and n is the length of list to be operated.
        ** note: like binary search applied on numbers list, the string list has to be sorted before you can invoke remove() function
    '''


    l_copy = list_string
    middle_index = len(list_string)//2
    if_deleted = False
    target_index = middle_index
    while l_copy:
        string_seq_middle = l_copy[middle_index] # get the middle item ()

        # comparing every char in sequence going to be remove from the list
        i = 0
        for j in range(len(string)):
            try:
                string_seq_middle[j]
            except:
                l_copy = l_copy[middle_index:]
                middle_index = len(l_copy)//2
                target_index += middle_index
            
            if ord(string[j]) < ord(string_seq_middle[j]):
                l_copy = l_copy[:middle_index]
                middle_index = len(l_copy)//2
                if len(l_cype)%2 == 1:
                    target_index -= 1
                    target_index -= middle_index
                else:
                    target_index -= middle_index
                break
            
            if ord(string[j]) > ord(string_seq_middle[j]):
                l_copy = l_copy[middle_index:]
                middle_index = len(l_copy)//2
                target_index += middle_index
                break
            i += 1
        if i == len(string):
            x = list_string.pop(target_index)
            if_deleted = True
            return ((x, target_index),list_string)
    return if_deleted

string_list = ["john","alex","helen","allen","james", "charly", "harry", "tom", "jerry"]
sorted_l = insert_sort(string_list) # sorting before binary search and remove.
l = remove("helen",sorted_l)
print(l)

        

