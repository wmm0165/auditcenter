# 肌酐清除率计算公式（成人）- 计算公式一
def ccr_calculate1(sex, unit, age, weight, scr):
    if unit == 'mg/dl':
        c = ((140 - age) * weight) / (72 * scr)
    else:
        c = ((140 - age) * weight) / (0.818 * scr)
    if sex == '男':
        ccr = c
    else:
        ccr = 0.85 * c
    return ccr


a = ccr_calculate1('女', 'mg/dl', 24, 60, 3)
print("ccr=%.4f" % a)
