from common.log_set import log

counter = 0
rerun_counter = {}
current_test_case = []


# 定义计数器
def count(data, case_name):
    global counter, current_test_case
    separator = '>' * 20
    if case_name not in rerun_counter:
        counter += 1
        rerun_counter[case_name] = 0
        current_test_case = counter
        yellow_text = f"\033[33m\033[1m{separator} 执行第{current_test_case}条用例 - {case_name}{separator} \033[0m"
        print_data = f"\n{yellow_text}\n"
    else:
        rerun_counter[case_name] += 1  # 增加该用例的重跑次数
        yellow_text = f"\033[33m\033[1m{separator}执行第{current_test_case}条失败用例，当前重跑第{rerun_counter[case_name]}遍 - {case_name}{separator}\033[0m"
        print_data = f"\n{yellow_text}\n"

    log.info(print_data)
    return data


# 红色字体并加粗
def colorize_text(text, style='\033[1m\033[31m'):
    end_style = '\033[0m'
    return style + text + end_style
