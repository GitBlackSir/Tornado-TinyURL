# __Auth__  : @GitBlackSir
# __Date__  : 2018/5/3
# __Email__ : gitblacksir@gmail.com

list62 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 10进制转62进制
def _10to_62Base(n):
    x, y = divmod(n, 62)
    if x > 0:
        return _10to_62Base(x) + list62[y]
    else:
        return list62[y]

# 62进制转10进制
def _62to_10Base(s):
    sL = list(s)
    sL.reverse()
    result = 0
    for x in range(len(sL)):
        result = result + list62.index(sL[x]) * (62 ** x)
    return result