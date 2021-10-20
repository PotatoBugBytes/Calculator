from math import sqrt


def check(l):
    if "+" in l or "-" in l or "÷" in l or "×" in l:
        return False
    else:
        return True


def spliting(string):
    final = []
    for n in string:
        final.append(n)
    return final


def ones(ones, obj):
    if obj in ones:
        final = ones.split(obj)
        c = check(final[1])
        if c == True:
            return final[1]
        else:
            return "no"
    else:
        return "no"


def twos(ones, obj):
    if obj in ones:
        final = ones.split(obj)
        c = check(final[0])
        if c == True:
            return final[0]
        else:
            return "no"
    else:
        return "no"


def removeone(string, remover):
    splited_string = spliting(string)
    splited_remover = spliting(remover)
    len_string = len(splited_string)
    for n in range(len_string):
        i = (n - (len_string - 1)) * (-1)
        for o in splited_remover:
            try:
                if o == splited_string[i]:
                    splited_string.pop(i)
                    splited_remover.remove(o)
                else:
                    pass
            except:
                pass
    return splited_string


def removesec(string, remover):
    splited_string = spliting(string)
    splited_remover = spliting(remover)
    len_rem = len(splited_remover)
    for _ in range(len_rem):
        if splited_remover[0] == splited_string[0]:
            splited_string.pop(0)
            splited_remover.pop(0)

    return splited_string


def sub(calcc):
    try:
        calc = "".join(calcc)
        d = calc.split("-", 1)
        if len(d) == 2:
            onee = str(d[0])
            twoo = str(d[1])
            if check(onee) == False:
                if ones(onee, obj="÷") == "no":
                    if ones(onee, obj="×") == "no":
                        if ones(onee, obj="+") == "no":
                            if ones(onee, "-") == "no":
                                pass
                            elif ones(onee, "-") != "no":
                                one = ones(d[0], "-")
                                d[0] = "".join(removeone(d[0], one))
                        elif ones(onee, "+") != "no":
                            one = ones(d[0], "+")
                            d[0] = "".join(removeone(d[0], one))
                    elif ones(onee, "×") != "no":
                        one = ones(d[0], "×")
                        d[0] = "".join(removeone(d[0], one))
                elif ones(onee, "÷") != "no":
                    one = ones(d[0], "÷")
                    d[0] = "".join(removeone(d[0], one))
            elif check(onee) == True:
                one = d[0]
                d[0] = "".join(removeone(d[0], one))
            if check(twoo) == False:
                if twos(twoo, "÷") == "no":
                    if twos(twoo, "×") == "no":
                        if twos(twoo, "+") == "no":
                            if twos(d[1], "-") == "no":
                                pass
                            elif twos(d[1], "-") != "no":
                                two = twos(d[1], "-")
                                d[1] = "".join(removesec(d[1], two))
                        elif twos(d[1], "+") != "no":
                            two = twos(d[1], "+")
                            d[1] = "".join(removesec(d[1], two))
                    elif twos(d[1], "×") != "no":
                        two = twos(d[1], "×")
                        d[1] = "".join(removesec(d[1], two))
                elif twos(d[1], "÷") != "no":
                    two = twos(d[1], "÷")
                    d[1] = "".join(removesec(d[1], two))
            elif check(twoo) == True:
                two = d[1]
                d[1] = "".join(removesec(d[1], two))
            dividend = float(one)
            divisor = float(two)
            ans = dividend - divisor
            ans = int(ans)
            ans = str(ans)
            d.insert(1, ans)
            calcc.clear()
            calcc.append("".join(d))
            return calcc
    except:
        return calcc


def div(calcc):
    try:
        calc = "".join(calcc)
        m = calc.split("÷", 1)
        if len(m) == 2:
            onee = str(m[0])
            twoo = str(m[1])
            if check(onee) == False:
                if ones(onee, "÷") == "no":
                    if ones(onee, obj="×") == "no":
                        if ones(onee, obj="+") == "no":
                            if ones(onee, obj="-") == "no":
                                pass
                            elif ones(onee, "-") != "no":
                                one = ones(m[0], "-")
                                m[0] = "".join(removeone(m[0], one))
                        elif ones(onee, "+") != "no":
                            one = ones(m[0], "+")
                            m[0] = "".join(removeone(m[0], one))
                    elif ones(onee, "×") != "no":
                        one = ones(m[0], "×")
                        m[0] = "".join(removeone(m[0], one))
                elif ones(onee, "÷") != "no":
                    one = ones(m[0], "÷")
                    m[0] = "".join(removeone(m[0], one))
            elif check(onee) == True:
                one = m[0]
                m[0] = "".join(removeone(m[0], one))
            if check(twoo) == False:
                if twos(twoo, obj="÷") == "no":
                    if twos(twoo, "×") == "no":
                        if twos(twoo, "+") == "no":
                            if twos(m[1], "-") == "no":
                                pass
                            elif twos(m[1], "-") != "no":
                                two = twos(m[1], "-")
                                m[1] = "".join(removesec(m[1], two))
                        elif twos(m[1], "+") != "no":
                            two = twos(m[1], "+")
                            m[1] = "".join(removesec(m[1], two))
                    elif twos(m[1], "×") != "no":
                        two = twos(m[1], "×")
                        m[1] = "".join(removesec(m[1], two))
                elif twos(m[1], "÷") != "no":
                    two = twos(m[1], "÷")
                    m[1] = "".join(removesec(m[1], two))
            elif check(twoo) == True:
                two = m[1]
                m[1] = "".join(removesec(m[1], two))
            num1 = float(one)
            num2 = float(two)
            ans = num1 / num2
            ans = int(ans)
            ans = str(ans)
            m.insert(1, ans)
        calcc.clear()
        calcc.append("".join(m))
        return calcc
    except:
        return calcc


def mult(calcc):
    try:
        calc = "".join(calcc)
        m = calc.split("×", 1)
        onee = str(m[0])
        twoo = str(m[1])
        if check(onee) == False:
            if ones(onee, obj="÷") == "no":
                print(232)
                if ones(onee, obj="×") == "no":
                    print(232)
                    if ones(onee, obj="+") == "no":
                        if ones(onee, "-") == "no":
                            pass
                        elif ones(onee, "-") != "no":
                            one = ones(m[0], "-")
                            m[0] = "".join(removeone(m[0], one))
                    elif ones(onee, "+") != "no":
                        one = ones(m[0], "+")
                        m[0] = "".join(removeone(m[0], one))
                elif ones(onee, "×") != "no":
                    print(232)
                    one = ones(m[0], "×")
                    m[0] = "".join(removeone(m[0], one))
            elif ones(onee, "÷") != "no":
                one = ones(m[0], "÷")
                m[0] = "".join(removeone(m[0], one))
        elif check(onee) == True:
            one = m[0]
            m[0] = "".join(removeone(m[0], one))
        if check(twoo) == False:
            if twos(twoo, obj="÷") == "no":
                if twos(twoo, "×") == "no":
                    if twos(twoo, "+") == "no":
                        if twos(m[1], "-") == "no":
                            pass
                        elif twos(m[1], "-") != "no":
                            two = twos(m[1], "-")
                            m[1] = "".join(removesec(m[1], two))
                    elif twos(m[1], "+") != "no":
                        two = twos(m[1], "+")
                        m[1] = "".join(removesec(m[1], two))
                elif twos(m[1], "×") != "no":
                    two = twos(m[1], "×")
                    m[1] = "".join(removesec(m[1], two))
            elif twos(m[1], "÷") != "no":
                two = twos(m[1], "÷")
                m[1] = "".join(removesec(m[1], two))
        elif check(twoo) == True:
            two = m[1]
            m[1] = "".join(removesec(m[1], two))
        num1 = float(one)
        num2 = float(two)
        ans = num1 * num2
        ans = int(ans)
        ans = str(ans)
        m.insert(1, ans)
        calcc.clear()
        calcc.append("".join(m))
        return calcc
    except:
        return calcc


def add(calcc):
    try:
        calc = "".join(calcc)
        m = calc.split("+", 1)
        if len(m) == 2:
            onee = str(m[0])
            twoo = str(m[1])
            if check(onee) == False:
                if ones(onee, obj="÷") == "no":
                    if ones(onee, obj="×") == "no":
                        if ones(onee, obj="+") == "no":
                            if ones(onee, "-") == "no":
                                pass
                            elif ones(onee, "-") != "no":
                                one = ones(m[0], "-")
                                m[0] = "".join(removeone(m[0], one))
                        elif ones(onee, "+") != "no":
                            one = ones(m[0], "+")
                            m[0] = "".join(removeone(m[0], one))
                    elif ones(onee, "×") != "no":
                        one = ones(m[0], "×")
                        m[0] = "".join(removeone(m[0], one))
                elif ones(onee, "÷") != "no":
                    one = ones(m[0], "÷")
                    m[0] = "".join(removeone(m[0], one))
            elif check(onee) == True:
                one = m[0]
                m[0] = "".join(removeone(m[0], one))
            if check(twoo) == False:
                if twos(twoo, obj="÷") == "no":
                    if twos(twoo, "×") == "no":
                        if twos(twoo, "+") == "no":
                            if twos(m[1], "-") == "no":
                                pass
                            elif twos(m[1], "-") != "no":
                                two = twos(m[1], "-")
                                m[1] = "".join(removesec(m[1], two))
                        elif twos(m[1], "+") != "no":
                            two = twos(m[1], "+")
                            m[1] = "".join(removesec(m[1], two))
                    elif twos(m[1], "×") != "no":
                        two = twos(m[1], "×")
                        m[1] = "".join(removesec(m[1], two))
                elif twos(m[1], "÷") != "no":
                    two = twos(m[1], "÷")
                    m[1] = "".join(removesec(m[1], two))
            elif check(twoo) == True:
                two = m[1]
                m[1] = "".join(removesec(m[1], two))
            num1 = float(one)
            num2 = float(two)
            ans = num1 + num2
            ans = int(ans)
            ans = str(ans)
            m.insert(1, ans)
        calcc.clear()
        calcc.append("".join(m))
        return calcc
    except:
        return calcc


def sqr(calcc):
    try:
        calc = "".join(calcc)
        m = calc.split("^", 1)
        if len(m) == 2:
            onee = str(m[0])
            twoo = str(m[1])
            if check(onee) == False:
                if ones(onee, obj="÷") == "no":
                    if ones(onee, obj="×") == "no":
                        if ones(onee, obj="+") == "no":
                            if ones(onee, "-") == "no":
                                pass
                            elif ones(onee, "-") != "no":
                                one = ones(m[0], "-")
                                m[0] = "".join(removeone(m[0], one))
                        elif ones(onee, "+") != "no":
                            one = ones(m[0], "+")
                            m[0] = "".join(removeone(m[0], one))
                    elif ones(onee, "×") != "no":
                        one = ones(m[0], "×")
                        m[0] = "".join(removeone(m[0], one))
                elif ones(onee, "÷") != "no":
                    one = ones(m[0], "÷")
                    m[0] = "".join(removeone(m[0], one))
            elif check(onee) == True:
                one = m[0]
                m[0] = "".join(removeone(m[0], one))
            if check(twoo) == False:
                if twos(twoo, obj="÷") == "no":
                    if twos(twoo, "×") == "no":
                        if twos(twoo, "+") == "no":
                            if twos(m[1], "-") == "no":
                                pass
                            elif twos(m[1], "-") != "no":
                                two = twos(m[1], "-")
                                m[1] = "".join(removesec(m[1], two))
                        elif twos(m[1], "+") != "no":
                            two = twos(m[1], "+")
                            m[1] = "".join(removesec(m[1], two))
                    elif twos(m[1], "×") != "no":
                        two = twos(m[1], "×")
                        m[1] = "".join(removesec(m[1], two))
                elif twos(m[1], "÷") != "no":
                    two = twos(m[1], "÷")
                    m[1] = "".join(removesec(m[1], two))
            elif check(twoo) == True:
                two = m[1]
                m[1] = "".join(removesec(m[1], two))
            num1 = float(one)
            num2 = float(two)
            ans = num1 ** num2
            ans = int(ans)
            ans = str(ans)
            m.insert(1, ans)
        calcc.clear()
        calcc.append("".join(m))
        return calcc
    except:
        return calcc

def sqrroot(calcc):
    try:
        calc = "".join(calcc)
        m = calc.split("²√", 1)
        if len(m) == 2:
            twoo = str(m[1])
            if check(twoo) == False:
                if twos(twoo, obj="÷") == "no":
                    if twos(twoo, "×") == "no":
                        if twos(twoo, "+") == "no":
                            if twos(m[1], "-") == "no":
                                pass
                            elif twos(m[1], "-") != "no":
                                two = twos(m[1], "-")
                                m[1] = "".join(removesec(m[1], two))
                        elif twos(m[1], "+") != "no":
                            two = twos(m[1], "+")
                            m[1] = "".join(removesec(m[1], two))
                    elif twos(m[1], "×") != "no":
                        two = twos(m[1], "×")
                        m[1] = "".join(removesec(m[1], two))
                elif twos(m[1], "÷") != "no":
                    two = twos(m[1], "÷")
                    m[1] = "".join(removesec(m[1], two))
            elif check(twoo) == True:
                two = m[1]
                m[1] = "".join(removesec(m[1], two))
            num2 = float(two)
            ans = sqrt(num2)
            ans = int(ans)
            ans = str(ans)
            m.insert(1, ans)
        calcc.clear()
        calcc.append("".join(m))
        return calcc
    except:
        return calcc

def fix(l):
    try:
        e = l[0]
        l.pop(0)
        for n in range(len(e)):
            l1 = len(e)
            l2 = l1-n
            l.insert(0,e[l2-1])
        return l
    except:
        return l

def d1(num=list):
    l = []
    num=fix(num)
    num.reverse()
    for n in range(0, 7):
        try:
            l.append(num[n])
        except:
            pass
    num.reverse()
    l.reverse()
    less = 7 - len(l)
    if less > 0:
        for _ in range(less):
            l.insert(0, "  ")
    else:
        pass
    return "".join(l)

def d2(num=list):
    l = []
    num.reverse()
    for n in range(7, 14):
        try:
            l.append(num[n])
        except:
            pass
    num.reverse()
    l.reverse()
    less = 7 - len(l)
    if less > 0:
        for _ in range(less):
            l.insert(0, "  ")
    else:
        pass
    return "".join(l)


def d3(num=list):
    l = []
    num.reverse()
    for n in range(14, 21):
        try:
            l.append(num[n])
        except:
            pass
    num.reverse()
    l.reverse()
    less = 7 - len(l)
    if less > 0:
        for _ in range(less):
            l.insert(0, " ")
    else:
        pass
    return "".join(l)


def d4(num):
    l = []
    num.reverse()
    for n in range(21, 28):
        try:
            l.append(num[n])
        except:
            pass
    num.reverse()
    l.reverse()
    less = 7 - len(l)
    if less > 0:
        for _ in range(less):
            l.insert(0, " ")
    else:
        pass
    return "".join(l)
