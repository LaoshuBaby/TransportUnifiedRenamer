preset_pattern={
    "1":"<ref><classifier><colon><from><arrow><to>"
}

def proposal_1(schema:int):
    if schema==1:
        return pass

def proposal_2(schema:int):
    if schema==1:
        return pass

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