students = {
    's1':{"name":"abhishek","surname":"bairagi","address":"neemuch"},
    "s2":{"name":'naman',"surname":"bairagi","address":"indor"},
    '''s3''':{"name":'sharukh',"surname":"khan","address":"Ratlam"},
}

for student in students:
    print(f'Hello {students[student]["name"]} {students[student]["surname"]} {students[student]["address"]}')