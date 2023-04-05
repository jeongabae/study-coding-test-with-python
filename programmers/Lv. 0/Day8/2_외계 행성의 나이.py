def solution(age):
    return ''.join([chr(int(a)+97) for a in str(age)]) #'a'의 아스키 코드 값은 97이므로..

    # #chr은 아스키 코드를 문자열로 변환 ex. chr(65)는 A
    # #ord는 문자열을 아스키코드로변환해줌 ex. ord('a')는 07