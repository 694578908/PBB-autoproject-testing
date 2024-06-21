counter = 0


# 定义计数器
def count(data):
    global counter
    separator = '>' * 20
    counter += 1  # 递增类级别的测试用例计数器
    yellow_text = f"\033[33m\033[1m{separator}执行第{counter}条用例{separator}\033[0m"
    print(f"\n{yellow_text}\n")
    return data


# 红色字体并加粗
def colorize_text(text, style='\033[1m\033[31m'):
    end_style = '\033[0m'
    return style + text + end_style