myUsers = ['Rykan','Tarik','collins','Memsi']
print('Enter a user name:')
name = input()
if name not in myUsers:
    print(name + 'is not a valid user')
else:
    print('Users name is ' + name)
    
