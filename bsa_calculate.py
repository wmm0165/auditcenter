def bsa_calculate(height, weight):

    if height == 0:
        if weight <= 30:
            bsa = weight * 0.035 + 0.1
        else:
            bsa = 1.05 + (weight - 30) * 0.02
    else:
        bsa = 0.0061 * height + 0.0128 * weight - 0.1529
    return bsa


if __name__ == '__main__':
    h = float(input("请输入身高："))
    w = float(input("请输入体重："))
    bsa = bsa_calculate(h, w)
    print("%.4f"%bsa)


