# 肌酐清除率计算公式（儿童）height(单位):m
def ccr_child(unit,height,scr):
    if unit == 'mg/dl':
        ccr = 41.3 * (height/scr)
    else:
        ccr = 41.3 * (height / (scr / 88.4))
    return ccr

a = ccr_child('m/dl',1.676,73.8)
print(a)