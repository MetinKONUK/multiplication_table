segments = []
for i in range(1,10):
    pseudo_list = []
    for x in range(1,10):
        text = "{} times {} is {}".format(i,x,i*x)
        pseudo_list.append(text)
    
    segments.append(pseudo_list)
for segment in segments:
    for text in segment:
        print(text)
    print("***************")
