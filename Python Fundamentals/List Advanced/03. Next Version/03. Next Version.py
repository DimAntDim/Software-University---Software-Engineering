"""

current_ver = input().split('.')
ver = ''.join(current_ver)
ver_1 = int(ver)+1
new_version = [i for i in str(ver_1)]
print('.'.join(new_version))
"""
# faster version:
current_ver = list(map(lambda x: int(x), input().split('.')))


def next_version(c_ver):
    if 0 <= c_ver[2] < 9:
        c_ver[2] += 1
        return c_ver
    else:
        c_ver[2] = 0
        if 0 <= c_ver[1] < 9:
            c_ver[1] += 1
            return c_ver
        else:
            c_ver[1] = 0
            if 0 <= c_ver[0] < 9:
                c_ver[0] += 1
                return c_ver


next_ver = [str(i) for i in next_version(current_ver)]
print('.'.join(next_ver))