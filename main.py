preset_pattern = {
    "1": [{
        "pattern": "<ref><classifier><colon><from><arrow><to>",
        "suitable_type": "*"
    }],
    "2": [{
        "pattern": "<type><ref><colon><from><arrow><to>",
        "suitable_type": "*"
    }],
    "3": [{
        "pattern": "<type><ref><classifier><colon><from><arrow><to>",
        "suitable_type": "*"
    }],
    "4": [{
        "pattern": "<network><ref><colon><from><arrow><to>",
        "suitable_type": "*"
    }],
    "5":[{
        "pattern":"<network><ref><colon><from><arrow><to>",
        "suitable_type":"subway"
    },{
        "pattern":"<type><ref><colon><from><arrow><to>",
        "suitable_type":"!subway"
    }]
}  # 这个由主页的方案预设1-7决定，照抄并加以符号化

topic_prefer = {
    "topic_3": "B",
    "topic_4": "甲",
    "topic_5": "子",
}  # 这个由用户选择议题三四五的标点符号习惯


def topic_3(schema: str, pattern: str):  # 作为修饰器，用于替换议题三的标点符号
    if schema == "A":
        return pattern.replace("<arrow>", "→")
    elif schema == "B":
        return pattern.replace("<arrow>", "->")
    elif schema == "C":
        return pattern.replace("<arrow>", "=>")
    else:
        return pattern


def topic_5(schema: str, pattern: str):  # 作为修饰器，用于替换议题五的标点符号
    if schema == "子":
        return pattern.replace("<colon>", ": ")
    elif schema == "丑":
        return pattern.replace("<colon>", "：")
    else:
        return pattern


def is_chinese_ref(ref: str):  # 判断是否包含中文，改为判断是否为纯ASCII的英文和数字
    try:
        if ref.decode("ascii").isalnum():
            return True
    except Exception as e:
        return False
    return False


def classifier(type: str, ref: str):
    if type == "bus":
        return "路"
    elif type == "subway":
        if is_chinese_ref(ref) == True:
            return "线"
        else:
            return "号线"
    else:
        return ""


def renamer(
    from_value: str,
    to_value: str,
    ref_value: str,
    type_value: str,
    network_value: str,
):
    pass


if __name__ == "__main__":
    renamer()
