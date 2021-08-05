# 모듈로 사용됨(library)
base =  2

def square(n):
    return base ** n

# 직접실행
if __name__ == '__main__':
    print(base)
    print(square(10))