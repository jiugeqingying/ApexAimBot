import configparser

_config_bit = configparser.ConfigParser()
# 从1bit.ai.config文件中读取参数和值
_config_bit.read("1bit.ai.config")

textGroup = 'group'  # 分组名称


def _write():
    with open("1bit.ai.config", "w") as f:
        _config_bit.write(f)
    pass


def set_config(key, value):
    value = str(value)  # 存入统一转字符串
    # 检查 textGroup 是否在 config 字典中
    if textGroup not in _config_bit:
        # 如果 textGroup 不存在，创建一个新的空字典
        _config_bit.setdefault(textGroup, {})
    # 将 key 和 value 存储到字典中
    _config_bit[textGroup][key] = value


def get_ini(key):
    try:
        value = _config_bit[textGroup][key]
        # 如果 value 是中文汉字,直接返回
        if all('\u4e00' <= char <= '\u9fff' for char in value):
            return value

            # 如果 value 是字符串且是整数,则返回整数
        elif isinstance(value, str) and value.isdigit():
            return int(value)

        # 如果 value 是字符串且有小数点,则返回浮点数
        elif isinstance(value, str) and '.' in value and all(char.isdigit() or char == '.' for char in value):
            return float(value)

        # 其他情况直接返回原值
        return value
    except KeyError:
        print(key, '未知的值')
        return 0  # 没找到值则返回0

