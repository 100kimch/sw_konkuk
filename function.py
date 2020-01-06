def print_address(name):
    print("서울특별시 광진구 능동로 120")
    print("새천년관 1006호")
    print(name)
    


def calculate_area (radius):    #원의 반지름을 입력받아 면적을 반환하는 함수
    area = 3.14 * radius**2
    return area

c_area = calculate_area(5.0)    #함수 호출
print("면적=",c_area)           #원의 면적 출력

