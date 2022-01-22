sample_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sample_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sample_list2 = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
#
#
# def snail(snail_map: list):
#     all_num = []
#     for small_list in snail_map:
#         all_num.extend(small_list)
#     all_num_str = ''.join([str(elem) for elem in all_num])
#     final_str = f'{all_num_str[:3]}{all_num_str[5]}{all_num_str[-1]}{all_num_str[-2:-4:-1]}{all_num_str[3:5]}'
#     return list([int(elem) for elem in final_str])
#
#
# print(snail(sample_list))
# print(snail(sample_list1))
# print(snail(sample_list2))


def snail(snail_map: list):
    result = []
    while snail_map:

        for element in snail_map[0]:
            result.append(element)
        snail_map.remove(snail_map[0])

        if not snail_map:
            break

        for element in snail_map:
            result.append(element.pop())

        if not snail_map:
            break

        snail_map[-1].reverse()

        for element in snail_map[-1]:
            result.append(element)
        snail_map.remove(snail_map[-1])

        if not snail_map:
            break

        snail_map.reverse()

        for element in snail_map:
            element.reverse()
            result.append(element.pop())
            element.reverse()

        snail_map.reverse()

    return result


print(snail(sample_list))
print(snail(sample_list1))
print(snail(sample_list2))
