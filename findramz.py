def jame_argam(ramz_digits):
    sumDigits = 0
    for k in ramz_digits:
        sumDigits += ramz_digits[k]
    return sumDigits

def ramz_is_ok(ramz_digits):
    if ramz_digits["panj"] + ramz_digits["se"] == 14 and \
    ramz_digits["yek"] == ramz_digits["do"]*2-1 and ramz_digits["chahar"] == ramz_digits["do"]+1 and \
    ramz_digits["se"] + ramz_digits["do"] == 10:
        if jame_argam(ramz_digits) == 30:
            return True

for ramz in range(0,100000):
    this_ramz = str(ramz).zfill(5)

    

    ramz_digits = {}
    ramz_digits["yek"] = int(this_ramz[0])
    ramz_digits["do"] = int(this_ramz[1])
    ramz_digits["se"] = int(this_ramz[2])
    ramz_digits["chahar"] = int(this_ramz[3])
    ramz_digits["panj"] = int(this_ramz[4])
    if ramz_is_ok(ramz_digits):
        print("Line 26: ",ramz)
