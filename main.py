preset_pattern={
    "1":"<ref><classifier><colon><from><arrow><to>"
}

topic_prefer={
    "topic_3":"B",
    "topic_4":"甲",
    "topic_5":"子"
}

def topic_3(schema:str,pattern:str):
    if schema=="A":
        return pattern.replace("<arrow>","→")
    elif schema=="B":
        return pattern.replace("<arrow>","->")
    elif schema=="C":
        return pattern.replace("<arrow>","=>")
    else:
        return pattern

def is_chinese_ref(ref:str):
    pass

def classifier(type:str,ref:str):
    if type=="bus":
        return "路"
    elif type=="subway":
        if is_chinese_ref(ref)==True:
            return "线"
        else:
            return "号线"
    else:
        return ""

def renamer(from:str, to:str, ref:str, type:str, network:str):


if __name__ == '__main__':
    renamer()