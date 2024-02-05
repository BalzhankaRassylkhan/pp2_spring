def balzhan(input_list):
    unique_list = []
    for i in input_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
my_list=list(input().split())
result_list = balzhan(my_list)
print(result_list)