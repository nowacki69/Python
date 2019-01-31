people = ['Charlie','Casey','Cody','Carly','Christina']
print(all(name[0]=='C' for name in people))

people.append('Kristy')
print(all(name[0]=='C' for name in people))

print(any(name[0]=='C' for name in people))
