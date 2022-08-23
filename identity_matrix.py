def id_mtrx(n) -> list:
    try:
        int_n = int(float(n))
    except ValueError:
        return []
    _return = []
    i = 0
    row = abs(int_n)
    while i < row:
        _row = []
        j = 0
        while j < row:
            _row.append(0)
            j += 1
        _row[i] = 1
        _return.append(_row)
        i += 1
    if int_n < 0:
        newlist = _return[::-1]
        return newlist
    return _return

print(id_mtrx('3'))
print(id_mtrx(-2))
print(id_mtrx(0))
