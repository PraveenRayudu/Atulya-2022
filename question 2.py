def masking(number):
    strnumber = str(number)
    strlength = len(strnumber)
    masked = strlength - 4
    slimstr = strnumber[masked:]
    print("*" * masked + slimstr)

masking(14678903583345)
