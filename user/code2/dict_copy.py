src_dict = {
    'a' : 1,
    'b' : 2,
    'c' : range(0, 10),
    'd' : {
        'name' : 1,
        'age' : 2,
        'score' : 3 
    }
}

dest_dict = {}

for key in src_dict:
    #key, src_dict[key]
    dest_dict[key] = src_dict[key]

print dest_dict

dest_dict2 = {}
#for xxx in src_dict.items()
    #xxx => (key, value)
    #xxx[0], xxx[1]
    #key, value = xxx[0], xxx[1]
    #key, value = xxx

for key, value in src_dict.items():
    dest_dict2[key] = value

print dest_dict2

dict(zip(src_dict.keys(), src_dict.values()))