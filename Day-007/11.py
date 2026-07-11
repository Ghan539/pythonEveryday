stud={
    "name":"ghanshyam",
    "subject":{
        "maths": 90,
        "science": 80,
        "english": 70,
        "hindi": 60,
        "social": 50
    },
    }
stud.update({"city":"jaipur"})
print(stud) 

new_dict = {"city":"jaipur","state":"rajasthan","pincode":302017}    
stud.update(new_dict)
print(stud)