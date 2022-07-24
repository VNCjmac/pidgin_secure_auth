### HASHBROWNS COMBINED MODULE ###

# import friar.py
# friar.hashbrowns1()("Your text you want to encrypt")
# ^ Yes above, there must be double parentheses to call the wrapper function


def hashbrowns1():
    modif1=96
    modif2=47
    modif3=81
    modif4=32

    def sec0(arg0):
        return len(arg0)
    def sec1(arg1):
        sub=15
        if sub > arg1:
            return sub - arg1
        elif arg1 > sub:
            return arg1 - sub
        else:
            return 94
    def sec2(arg2):
        sub=93
        if sub > arg2:
            return sub - arg2
        elif arg2 > sub:
            return arg2 - sub
        else:
            return 102
    def sec3(arg3):
        sub=57
        if sub > arg3:
            return sub-arg3
        elif arg3 > sub:
            return arg3 - sub
        else:
            return 39
    def arg0(str0):
        buff=[]
        for arg in str0:
            buff.append(ord(arg))
        return [arg11%modif1 for arg11 in buff]
    def arg2(buff0):
        phldr0=[]
        for int0 in buff0:
            phldr0.append(int0%modif2)
        return phldr0
    def arg3(buff1):
        phldr1=[]
        for int1 in buff1:
            phldr1.append(int1%modif3)
        return phldr1
    def arg4(buff2):
        phldr2=[]
        for int2 in buff2:
            phldr2.append(int2%modif4)
        return phldr2
    
    def hashbrownsc1(txt):
        mult=13
        hshval=[]
        a=arg0(txt)
        b=arg2(a)
        c=arg3(b)
        d=arg4(c)
        d.insert(0, sec1(sec0(txt)))
        d.insert(sec0(txt)%3, sec3(sec0(txt)))
        d.insert(sec0(txt)-1, sec2(sec0(txt)))
        d[sec0(txt)-2]=d[sec0(txt)]*mult
        for x in d:
            hshval.append(chr(x << 8))
        return "".join(hshval)

    return hashbrownsc1

def hashbrowns2():
    modif1=39
    modif2=50
    modif3=61
    modif4=72

    def patch0():
        def wrap0(arg155):
            arg23=[]
            for arg11 in arg155:
                arg23.append(chr(ord(arg11) << 3))
            return "".join(arg23)
        return wrap0
    def unit0(vsg113):
        return patch0()(vsg113)
    def sec0(arg0):
        return len(arg0)
    def sec1(arg1):
        sub=15
        if sub > arg1:
            return sub - arg1
        elif arg1 > sub:
            return arg1 - sub
        else:
            return 94
    def sec_p5(arglen):
        sub=37
        if sub > arglen:
            return sub - arglen
        elif arglen > sub:
            return arglen - sub
        else:
            return sub+54-31
    def sec2(arg2):
        sub=93
        if sub > arg2:
            return sub - arg2
        elif arg2 > sub:
            return arg2 - sub
        else:
            return 102
    def sec3(arg3):
        sub=57
        if sub > arg3:
            return sub-arg3
        elif arg3 > sub:
            return arg3 - sub
        else:
            return 39
    def arg0(str0):
        buff=[]
        for arg in str0:
            buff.append(ord(arg))
        return [arg11%modif1 for arg11 in buff]
    def arg2(buff0):
        phldr0=[]
        for int0 in buff0:
            phldr0.append(int0%modif2)
        return phldr0
    def arg3(buff1):
        phldr1=[]
        for int1 in buff1:
            phldr1.append(int1%modif3)
        return phldr1
    def arg4(buff2):
        phldr2=[]
        for int2 in buff2:
            phldr2.append(int2%modif4)
        return phldr2
    def sec32(arg32):
        secnum=sec3(sec0(arg32))
        return arg32.replace(" ", str(chr(secnum)))
    def hashbrownc1(arg15):
        mult=13
        txt=sec32(arg15)
        hshval=[]
        a=arg0(txt)
        b=arg2(a)
        c=arg3(b)
        d=arg4(c)
        d.insert(0, sec1(sec0(txt)))
        d.insert(sec0(txt)%3, sec3(sec0(txt)))
        d.insert(sec0(txt)-1, sec2(sec0(txt)))
        d[sec0(txt)-2]=d[sec0(txt)]*mult
        for x in d:
            hshval.append(chr(x << 8))
        return unit0(str(sec0(txt)))+"".join(hshval)+"=="

    def hashbrownc2(argh0):
        secit=hashbrownc1(argh0)
        thrit=hashbrownc1(secit)
        frit=hashbrownc1(thrit)
        a211=hashbrownc1(frit)
        return a211

    return hashbrownc2

def hashbrowns3():
    modif1=39
    modif2=50
    modif3=61
    modif4=72

    def patch0():
        def wrap0(arg155):
            arg23=[]
            for arg11 in arg155:
                arg23.append(chr(ord(arg11) << 3))
            return "".join(arg23)
        return wrap0
    def unit0(vsg113):
        return patch0()(vsg113)
    def sec0(arg0):
        return len(arg0)
    def sec1(arg1):
        sub=15
        if sub > arg1:
            return sub - arg1
        elif arg1 > sub:
            return arg1 - sub
        else:
            return 94
    def sec_p5(arglen):
        sub=37
        if sub > arglen:
            return sub - arglen
        elif arglen > sub:
            return arglen - sub
        else:
            return sub+54-31
    def sec2(arg2):
        sub=93
        if sub > arg2:
            return sub - arg2
        elif arg2 > sub:
            return arg2 - sub
        else:
            return 102
    def sec3(arg3):
        sub=57
        if sub > arg3:
            return sub-arg3
        elif arg3 > sub:
            return arg3 - sub
        else:
            return 39
    def arg0(str0):
        buff=[]
        for arg in str0:
            buff.append(ord(arg))
        return [arg11%modif1 for arg11 in buff]
    def arg2(buff0):
        phldr0=[]
        for int0 in buff0:
            phldr0.append(int0%modif2)
        return phldr0
    def arg3(buff1):
        phldr1=[]
        for int1 in buff1:
            phldr1.append(int1%modif3)
        return phldr1
    def arg4(buff2):
        phldr2=[]
        for int2 in buff2:
            phldr2.append(int2%modif4)
        return phldr2
    def sec32(arg32):
        secnum=sec3(sec0(arg32))
        return arg32.replace(" ", str(chr(secnum)))
    def hashbrownc1(arg15):
        mult=13
        txt=sec32(arg15)
        hshval=[]
        a=arg0(txt)
        b=arg2(a)
        c=arg3(b)
        d=arg4(c)
        d.insert(0, sec1(sec0(txt)))
        d.insert(sec0(txt)%3, sec3(sec0(txt)))
        d.insert(sec0(txt)-1, sec2(sec0(txt)))
        d[sec0(txt)-2]=d[sec0(txt)]*mult
        for x in d:
            hshval.append(chr(x << 7))
        return unit0(str(sec0(txt)))+"".join(hshval)+"=="

    def hashbrownc2(argh0, arglen):
        buff=[]
        buff.append(hashbrownc1(argh0))
        for i in range(arglen):
            res=hashbrownc1(buff[0])
            buff.clear()
            buff.append(res)
        return buff[0]

    def hashbrownc3(arg54):
        return hashbrownc2(str(arg54), sec0(str(arg54)))

    return hashbrownc3