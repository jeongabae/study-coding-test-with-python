def solution(babbling):
    cnt = 0
    for i in babbling:
        for j in ["aya", "ye", "woo", "ma"]:
            i=i.replace(j,".")
        i=i.replace(".","")
        if i=="": cnt+=1
    return cnt