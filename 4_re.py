import re


def print_match(m):
    if m:
        print('m.group():', m.group())
        print('m.string:', m.string)
        print('m.start():', m.start())
        print('m.end():', m.end())
        print('m.span():', m.span())
    else:
        print('No Match')


# pattern = re.compile('ca.e')
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de)  : 문자열의 시작
# $ (se$)  : 문자열의 끝

# m = pattern.match('good care'): 주어진 문자열의 '처음부터' 일치하는지 확인
# m = pattern.search('good care'): 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)
# lst = pattern.findall('good care cafe'): 일치하는 모든 것을 '리스트' 형태로 반환
# print(lst)
