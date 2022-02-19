preset_pattern=[
    "",
    "",
]

def is_chinese_ref(ref:str):
    if ref.find("路")!=-1 or ref.find("号")!=-1:
        return True
    else:
        return False

def classifier(type:str,ref:str):
    if type=="bus":
        return "路"
    elif type=="subway":
        if ref.

def renamer(from:str, to:str, ref:str, type:str, network:str):


if __name__ == '__main__':
    renamer()