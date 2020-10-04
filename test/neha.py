def countForNeha(district_count, start_char, end_char, start_num, end_num):
    letter_count = ord(end_char)-ord(start_char)+1
    letter_combination = letter_count*(letter_count-1) 

    num_count = end_num-start_num+1
    num_combination = num_count**4

    special_count = num_count + num_count*(num_count-1)*4

    print(district_count*letter_combination*(num_combination-special_count))

district_count = int(input())
start_char, end_char = input().split()
start_num, end_num = list(map(int, input().split()))
countForNeha(district_count, start_char, end_char, start_num, end_num)
# countForNeha(1, 'A', 'B', 1, 4)