class student:

    def __init__(self,fullname):
        self.name=fullname
        print("adding a new student in database.")

s1=student("karan")
s2=student("ghanshyam")
s3=student("ramesh")
print(s1.name)        
print(s2.name)
print(s3.name)