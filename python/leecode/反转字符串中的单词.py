"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:
输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格
"""


def reverse_words(s: str) -> str:
    split_list = s.split(" ")
    result_list = []
    for i in split_list:
        list_i = [j for j in i]
        list_i.reverse()
        new_i = "".join(list_i)
        result_list.append(new_i)
    new_s = " ".join(result_list)
    return new_s


print(reverse_words("Let's take LeetCode contest"))

