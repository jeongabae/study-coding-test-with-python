def solution(id_pw, db):
    for i in db:
        if id_pw[0]==i[0]:
            if id_pw[1]==i[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"

"""
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        print(db_pw)
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"
"""
