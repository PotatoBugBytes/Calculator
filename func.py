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


def floatingthree(num1):
    fnum = []
    num = spliting(num1)
    try:
        for n in range(3):
            fnum.append(num[n])
        return fnum
    except:
        for n in range(2):
            fnum.append(num[n])
        return fnum
    finally:
        fnum.append(num1)
        return num1


def floating(num):
    num = str(num)
    num = num.split(".")
    num1 = num[0]
    num2 = num[1]
    num2 = floatingthree(num2)
    ans = (f"{num1}.{num2}")
    return ans


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
        if "-" in calcc[0] or "-" in calcc:
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
                ans = str(ans)
                anss = spliting(ans)
                if anss[len(anss) - 1] == "0":
                    ans1 = "".join(anss)
                    ans1 = float(ans1)
                    ans1 = int(ans1)
                    ans1 = str(ans1)
                    d.insert(1, ans1)
                    calcc.clear()
                    calcc.append("".join(d))
                    return calcc
                elif anss[len(anss) - 1] != "0":
                    ansdot = ans.split(".")
                    ans1 = "".join(anss)
                    ans1 = floating(float(ans1))
                    ans1 = str(ans1)
                    d.insert(1, ans1)
                    calcc.clear()
                    calcc.append("".join(d))
                    return calcc
        else:
            return calcc
    except:
        return calcc


def div(calcc):
    try:
        if "÷" in calcc[0] or "÷" in calcc:
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
                ans = str(ans)
                anss = spliting(ans)
                if anss[len(anss) - 1] == "0":
                    ans1 = "".join(anss)
                    ans1 = float(ans1)
                    ans1 = int(ans1)
                    ans1 = str(ans1)
                    m.insert(1, ans1)
                    calcc.clear()
                    calcc.append("".join(m))
                    return calcc
                elif anss[len(anss) - 1] != "0":
                    ansdot = ans.split(".")
                    ans1 = "".join(anss)
                    ans1 = floating(float(ans1))
                    ans1 = str(ans1)
                    m.insert(1, ans1)
                    calcc.clear()
                    calcc.append("".join(m))
                    return calcc
        else:
            return calcc
    except:
        return calcc


def mult(calcc):
    try:
        if "×" in calcc[0] or "×" in calcc:
            calc = "".join(calcc)
            m = calc.split("×", 1)
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
            ans = num1 * num2
            ans = str(ans)
            anss = spliting(ans)
            if anss[len(anss) - 1] == "0":
                ans1 = "".join(anss)
                ans1 = float(ans1)
                ans1 = int(ans1)
                ans1 = str(ans1)
                m.insert(1, ans1)
                calcc.clear()
                calcc.append("".join(m))
                return calcc
            elif anss[len(anss) - 1] != 0:
                ansdot = ans.split(".")
                ans1 = "".join(anss)
                ans1 = floating(float(ans1))
                ans1 = str(ans1)
                m.insert(1, ans1)
                calcc.clear()
                calcc.append("".join(m))
                return calcc
        else:
            return calcc
    except:
        return calcc


def add(calcc):
    try:
        if "+" in calcc[0] or "+" in calcc:
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
                ans = str(ans)
                anss = spliting(ans)
                if anss[len(anss) - 1] == "0":
                    ans1 = "".join(anss)
                    ans1 = float(ans1)
                    ans1 = int(ans1)
                    ans1 = str(ans1)
                    m.insert(1, ans1)
                    calcc.clear()
                    calcc.append("".join(m))
                    return calcc
                elif anss[len(anss) - 1] != 0:
                    ansdot = ans.split(".")
                    ans1 = "".join(anss)
                    ans1 = floating(float(ans1))
                    ans1 = str(ans1)
                    m.insert(1, ans1)
                    calcc.clear()
                    calcc.append("".join(m))
                    return calcc
        else:
            return calcc
    except:
        return calcc


def sqr(calcc):
    try:
        if "^" in calcc[0] or "^" in calcc:
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
                ans = str(ans)
                anss = spliting(ans)
                if anss[len(anss) - 1] == "0":
                    ans1 = "".join(anss)
                    ans1 = float(ans1)
                    ans1 = int(ans1)
                    ans1 = str(ans1)
                    m.insert(1, ans1)
                    calcc.clear()
                    calcc.append("".join(m))
                    return calcc
                elif anss[len(anss) - 1] != 0:
                    ansdot = ans.split(".")
                    ans1 = "".join(anss)
                    ans1 = floating(float(ans1))
                    ans1 = str(ans1)
                    m.insert(1, ans1)
                    calcc.clear()
                    calcc.append("".join(m))
                    return calcc
        else:
            return calcc
    except:
        return calcc


def sqrroot(calcc):
    try:
        if "²√" in calcc[0] or "²√" in calcc:
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
                ans = str(ans)
                anss = spliting(ans)
                if anss[len(anss) - 1] == "0":
                    ans1 = "".join(anss)
                    ans1 = float(ans1)
                    ans1 = int(ans1)
                    ans1 = str(ans1)
                    m.insert(1, ans1)
                    calcc.clear()
                    calcc.append("".join(m))
                    return calcc
                elif anss[len(anss) - 1] != 0:
                    ansdot = ans.split(".")
                    ans1 = "".join(anss)
                    ans1 = floating(float(ans1))
                    ans1 = str(ans1)
                    m.insert(1, ans1)
                    calcc.clear()
                    calcc.append("".join(m))
                    return calcc
        else:
            return calcc
    except:
        return calcc


def fix(l):
    try:
        e = l[0]
        l.pop(0)
        for n in range(len(e)):
            l1 = len(e)
            l2 = l1 - n
            l.insert(0, e[l2 - 1])
        return l
    except:
        return l


def d1(num=list):
    l = []
    num = fix(num)
    num.reverse()
    for n in range(0, 30):
        try:
            l.append(num[n])
        except:
            pass
    num.reverse()
    l.reverse()
    less = 30 - len(l)
    if less > 0:
        for _ in range(less):
            l.insert(0, "  ")
    else:
        pass
    return "".join(l)




def c2(l):
    calc0 = sqrroot(l)
    calc10 = calc0.copy()
    calc1 = sqr(calc0)
    calc2 = div(calc1)
    calc3 = mult(calc2)
    calc4 = add(calc3)
    calc5 = sub(calc4)
    if "×" in calc10 or "+" in calc10 or "-" in calc10 or "÷" in calc10 or "^" in calc10 or "²√" in calc10:
        if calc10==calc5:
            return "0"
        else:
            return "1"
    else:
        return "1"
