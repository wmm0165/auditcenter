import math
from decimal import Decimal
# 肌酐清除率计算公式（成人）- 计算公式二

class CalculateCcr:
    """年龄≥16岁 """

    def exprCCR(self, unit, sex, Scr, age):
        ccr = 0.0
        eGFR = 0.0

        # 输入体重
        weight = 60
        # 输入身高
        height = 1.6
        BMI = weight / (height * height)
        print("BMI=%f" % BMI)
        BSA = 0.0061 * height * 100 + 0.0128 * weight - 0.1529
        print("BSA=%f" % BSA)

        if 16 <= age <= 18:
            temp = ((140 - age) * weight) / (0.818 * Scr)
            # scr单位为mg/dl
            if unit == 'mg/dl':
                ccr = ((140 - age) * weight) * 1.0 / (72 * Scr)
                if (sex == '女'):
                    ccr = ccr * 0.85
                ccr = round(ccr, 4)
            # 单位为μmol/L(umol/L)
            else:
                if sex == '男':
                    ccr = round(temp, 4)
                else:
                    ccr = round(temp * 0.85, 4)
        else:
            # 判断单位
            # scr单位为mg/ml
            if unit == 'mg/dl':
                if sex == '女':
                    if (Scr <= 0.7):
                        eGFR = 144 * ((Scr / 0.7) ** (-0.329)) * (0.993 ** age)
                    else:
                        eGFR = 144 * ((Scr / 0.7) ** (-1.209)) * (0.993 ** age)
                else:
                    if (Scr <= 0.9):
                        eGFR = 141 * ((Scr / 0.9) ** (-0.411)) * (0.993 ** age)
                    else:
                        eGFR = 141 * ((Scr / 0.9) ** (-1.209)) * (0.993 ** age)

            # scr单位为μmol/L(umol/L)
            else:
                if sex == '女':
                    if Scr <= 61.88:
                        eGFR = 144 * ((Scr / (0.7 * 88.4)) ** (-0.329)) * (0.993 ** age)
                    else:
                        eGFR = 144 * ((Scr / (0.7 * 88.4)) ** (-1.209)) * (0.993 ** age)

                else:
                    if Scr <= 79.56:
                        eGFR = 141 * ((Scr / (0.9 * 88.4)) ** (-0.411)) * (0.993 ** age)
                    else:
                        eGFR = 141 * ((Scr / (0.9 * 88.4)) ** (-1.209)) * (0.993 ** age)
            # 当18.5mg/m2≤BMI≤25mg/m2时
            if 18.5 <= BMI <= 25:
                ccr = round(eGFR, 4)
            else:
                ccr = round((eGFR * BSA * 1.0 / 1.73), 4)
        return ccr


a = CalculateCcr()
print(a.exprCCR('mg/dl', '男', 1, 24))  # umol/L  μmol/L mg/dl
