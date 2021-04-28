string_list = ["john","alex","helen","allen","james", "charly", "harry", "tom", "jerry"]
l = ["tom", "jerry"]




def insert_sort(l):

    '''
    function consists of a search method with underlying intuition of binary search to sort list of string with alpabet descending order.
        searching process:
            we have a list of string l
            let m indicates the length of the string sequence which we are going to insert to list l,
            let n indicates the length of the list of string l,
            the searching algorithm, in worst case will run in time O(m*log(n))
        ***note: because it is rarely in real-life to insert a string-seq to a list of string-seq where every string-seq consists of huge (let us see more than 20 chars),
                 the m can be think of as a consistent value, then the time complexity of this algorithm would be O(log(n))

        whole insert sorting process:
            let t indicates the number of string-sequence we wanna sort,
            the whole insert sort process will run in time O(t*m*log(n)),
 
    '''
    sorted_l = [l.pop()]
    while l:
    # for every word / string sequence in the list, do:
        print(l)
        # 1. get the word:
        temp_sequence = l.pop()
        
        # 2. binary search word
        l_copy = sorted_l
        middle_index = len(l_copy)//2
        while l_copy:
            print(l_copy, middle_index)
            # 3. compare every word with the word at middle of the list l_copy 
            loop_No = 0
            w = l_copy[middle_index]
            turn_direction = None # used to recognize the next subset is right or left of current set.
            for i in range(len(temp_sequence)):
            # for every char in the word, do:
                # 3.1 if word in list is short than word being inserted, do:
                try: 
                    l_copy[middle_index][i]
                except:
                    l_copy = l_copy[middle_index:]
                    turn_direction = "RIGHT"
                    middle_index = len(l_copy)//2
                    break
                # 3.2 compare char a = temp_sequence[i] with char b = l_copy[middke_index][i]:
                #   if a == b, do nothing
                #   if ASCII(a) < ASCII(b), update l_copy with its left half sub-list, and update new middle_index, 
                #                           compare current word (temp_sequence) with next word (next half's middle word)
                if ord(temp_sequence[i]) < ord(l_copy[middle_index][i]):
                    l_copy = l_copy[:middle_index]
                    turn_direction = "LEFT"
                    middle_index = len(l_copy)//2
                    break

                #   if ASCII(a) > ASCII(b), update l_copy with its lerightft half sub-list, and update new middle_index,
                #                           compare current word (temp_sequence) with next word (next half's middle word)
                if ord(temp_sequence[i]) > ord(l_copy[middle_index][i]):
                    l_copy = l_copy[middle_index:]
                    turn_direction = "RIGHT"
                    middle_index = len(l_copy)//2
                    break
                loop_No += 1
            # 4. after loop chars in temp_sequence,
            #   4.1 if loop No. is same as len(temp_sequence), means that the temp_sequence is subsequence of the word at middle of l_copy, insert it before current middle word,do:
            #print(loop_No,turn_direction,len(l_copy))
            if loop_No == len(temp_sequence):
                sorted_l.insert(sorted_l.index(w),temp_sequence)
                break
            else:   
                if turn_direction == "LEFT":
                    if len(l_copy) == 0:
                        sorted_l.insert(sorted_l.index(w),temp_sequence)
                        break
                else:
                    if len(l_copy) == 1:
                        sorted_l.insert(sorted_l.index(w) + 1,temp_sequence)
                        break

            #   4.2 if loop No. is not the same as len(temp_sequence), means the chars in temp_sequence has not been completly compared, do:
    return sorted_l

print(insert_sort(string_list))

            
