import datetime
from college_data import fetch_data

LRUcache={}

def LRU_cahce():
    # least_called_id=0
    # least_recently_used_id=0
    # #update_the_
    pass

def update_cache():
    pass

def student_server(roll_no_,LRU):
    if LRU.has_key(roll_no_):
        print(LRUcache[roll_no_])
        # LRUcache[roll_no_]['LRU']['score']+=1

    else:
        n=fetch_data(roll_no_)
        print(n)
        LRUcache[roll_no_]=n






while(True):
    roll_no_=str(input('Enter you student id'))
    student_server(roll_no_,LRUcache)