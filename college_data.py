import time

# print(Student_data['26']['Name'])


def fetch_data(id):
    student_data = {'26': {'Name': 'Ravi Sankar Komati', 'Branch': 'Mechanical'},
                    '27': {'Name': 'Ravi Teja Kanta', 'Branch': 'Information Technology'}}
    time.sleep(9)
    return(student_data[id])