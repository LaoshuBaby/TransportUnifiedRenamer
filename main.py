pattern_preset = {
    "1": [
        {
            "pattern": "<ref><classifier><colon><from><arrow><to>",
            "suitable_type": "*",
        }
    ],
    "2": [
        {
            "pattern": "<type><space><ref><colon><from><arrow><to>",
            "suitable_type": "*",
        }
    ],
    "3": [
        {
            "pattern": "<type><space><ref><classifier><colon><from><arrow><to>",
            "suitable_type": "*",
        }
    ],
    "4": [
        {
            "pattern": "<network><space><ref><colon><from><arrow><to>",
            "suitable_type": "*",
        }
    ],
    "5": [
        {
            "pattern": "<network><space><ref><colon><from><arrow><to>",
            "suitable_type": "subway",
        },
        {
            "pattern": "<type><space><ref><colon><from><arrow><to>",
            "suitable_type": "!subway",
        },
    ],
    "6": "没看懂，咕了",
    "7": [
        {
            "pattern": "<network><space><ref><classifier><colon><from><arrow><to>",
            "suitable_type": "(subway|light_rail|monorail|tram)",
        },
        {
            "pattern": "<ref><classifier><colon><from><arrow><to>",
            "suitable_type": "!(subway|light_rail|monorail|tram)",
        },
    ],
}  # 这个由主页的方案预设1-7决定，照抄并加以符号化

topic_prefer = {
    "topic_1": "UNCHOOSEABLE BECAUSE OF DEFINED IN PATTERN",
    "topic_2": "UNCHOOSEABLE BECAUSE OF DEFINED IN PATTERN",
    "topic_3": "B",
    "topic_4": "甲",
    "topic_5": "子",
    "topic_6": "UNCHOOSEABLE BECAUSE OF THIS IS INPUT OF THIS PROGRAM",
}  # 这个由用户选择议题三四五的标点符号习惯


def topic_3(schema: str, pattern: str):  # 作为修饰器，用于替换议题三的标点符号
    if schema == "A":
        return pattern.replace("<arrow>", "→")
    elif schema == "B":
        return pattern.replace("<arrow>", "->")
    elif schema == "C":
        return pattern.replace("<arrow>", "=>")
    elif schema == "D":
        return pattern.replace("<arrow>", "-->")
    else:  # 漏网之鱼
        return pattern


def topic_4(schema: str, pattern: str):  # 作为修饰器，用于替换议题四的标点符号
    if schema == "甲":
        return pattern.replace("<space>", " ")
    else:  # 漏网之鱼
        return pattern


def topic_5(schema: str, pattern: str):  # 作为修饰器，用于替换议题五的标点符号
    if schema == "子":
        return pattern.replace("<colon>", ": ")
    elif schema == "丑":
        return pattern.replace("<colon>", "：")
    else:  # 漏网之鱼
        return pattern


def topic_6(type: str):  # 作为检查器，对一些传入的方便确定命名格式的类型fallback到OSM类型
    if type == "brt":  # 快速公交
        return ["bus", "[route=bus]"]
    elif type == "maglev":
        return ["monorail", "[route=monorail]+[monorail=maglev]"]
    elif type == "apm":
        return ["light_rail", "[route=light_rail]"]
    else:  # 漏网之鱼
        return [type, "[route=" + type + "]"]


def is_chinese_ref(ref: str):  # 判断是否包含中文
    for ch in check_str.decode("utf-8"):
        if u"\u4e00" <= ch <= u"\u9fff":
            return True
    return False


def classifier(type: str, ref: str):
    if type == "bus":
        return "路"
    elif type == "subway" or type == "brt":
        if is_chinese_ref(ref) == True:
            if "线" in ref:
                return ""
            else:
                return "线"
        else:
            return "号线"
    else:
        return ""


def unify(
    from_value: str,
    to_value: str,
    ref_value: str,
    type_value: str,
    network_value: str,
):
    pass


if __name__ == "__main__":
    # 测试样例1
    unify("模式口", "新首钢", "11", "subway", "北京地铁")
    # 测试样例2
    unify("巴沟", "香山", "西郊", "subway", "北京地铁")
    # 测试样例3
    unify("火车站", "全运媒体村", "BRT5", "brt", "济南公交")
    # 测试样例4
    unify("龙阳路", "浦东国际机场", "磁浮线", "maglev", "上海地铁")
    # 测试样例5
    unify("广州塔", "林和西", "APM", "apm", "广州地铁")
    # 测试样例6
    unify("砚泉", "大观园", "B103", "trolleybus", "济南公交")
    # 测试样例7
    unify("伪满皇宫", "长影世纪城", "3", "light_rail", "长春轨道交通")
