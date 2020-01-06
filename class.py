class Singer:                   # 가수 클래스 정의
    popularity = 100            # 속성은 변수로 설정: 인기도=100
    
    def sing(self):             # 동작은 매서드로 설정: 노래하기
        return "Lalala~"
    
BTS = Singer()                  # 가수인 BTS 객체 생성
IU = Singer()                   # 가수인 IU 객체 생성

