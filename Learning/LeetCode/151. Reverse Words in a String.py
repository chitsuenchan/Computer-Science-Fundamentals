# def reverseWords(s):
#     result = ""
#
#     word_list = s.split()[::-1]
#
#     for i in range(len(word_list)):
#
#         if i == len(word_list) - 1:
#             result += word_list[i]
#         else:
#             result += word_list[i] + " "
#
#     print(result)


def reverseWords(s):
    at_word = False
    reverse_lst = []
    sub_word = ""
    for char in s:

        if char != " " and at_word is False:
            sub_word = ""
            sub_word += char
            at_word = True

        elif char != " " and at_word is True:
            sub_word += char

        elif char == " " and at_word is True:
            reverse_lst.append(sub_word)
            at_word = False

    return " ".join(reverse_lst[::-1])


print(reverseWords("  hello world  "))
