from django.test import TestCase

# Create your tests here.
from django.core.paginator import Paginator

data_list = list('adfalksejrpqaodkdlkafjkjeqwormv')
print(len(data_list))

pn = Paginator(data_list, 5)    # 전체데이터, 한 페이지에 보여질 데이터수
print('총데이터수', pn.count)
print('총페이지수', pn.num_pages)  
print('페이지 범위', pn.page_range)

for page in pn.page_range:
    print(page, end='\t')

# 각 페이지에 데이터들 조회
# paginator.page(페이지 번호) - 번포헤이지의 데이터들을 (Page객체로) 반환
page1 = pn.page(1)    
print(type(page1), page1)    # page: 그 페이지의 데이터를 관리
print("이전 페이지 유무", page1.has_previous())  
print("다음 페이지 유무", page1.has_next())
page7 = pn.page(7)  
print("이전 페이지 유무-7", page7.has_previous())  
print("다음 페이지 유무-7", page7.has_next())


page3 = pn.page(3)  
print("이전 페이지 유무-3", page3.has_previous())  
print("다음 페이지 유무-3", page3.has_next())


# 이전/다음 페이지가 없는 경우 EmptyPage 예외 발생.
# page1.previous_page_number()

page_data = page1.object_list
print(type(page_data))
print(page_data)
print(page3.object_list)

##############################################

paginator = Paginator(data_list, 3)   # 한 페이지에 데이터 3개 씩 보여줄 것을 정의

for page_num in paginator.page_range:
    page = paginator.page(page_num)
    print(page_num)
    for data in page.object_list:    # 페이지 데이터를 추출해서 리스트에 넣은 것을 하나씩 출력
        print(data, end='\t')
    print('\n-----------------------------------------------------------')



#################### 페이지 번호 처리 #####################
current_page = 2    # 현재 페이지
page_numbers_range = 5    # 한 페이지그룹의 페이지 수
start_index = int((current_page-1)/page_numbers_range)*page_numbers_range
end_index = start_index + page_numbers_range
print(start_index, end_index)
print(paginator.page_range)
print(paginator.page_range[start_index:end_index])

for p in paginator.page_range[start_index:end_index]:
    print(p, end='\t')