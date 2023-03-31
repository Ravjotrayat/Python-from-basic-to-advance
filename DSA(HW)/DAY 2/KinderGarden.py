

def Text(text,voc):
    text=text.lower().split(' ')
    s=set()
    for i in text:
        if i in voc:
            continue
        else:
            s.add(i)
    print(s)
text="The sun rises in the east"
voc=["sun","in","east","doctor","day"]
Text(text,voc)
