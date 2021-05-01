vip_list = set()
regular_list = set()
presented_vip = set()
presented_regular = set()


def input_lines(count):

    for _ in range(count):
        guest = input()
        if guest[0].isdigit():
            vip_list.add(guest)
        else:
            regular_list.add(guest)
    return vip_list, regular_list, party_list()


def party_list():
    while True:
        code = input()
        if code == 'END':
            break
        else:
            if code[0].isdigit():
                presented_vip.add(code)
            else:
                presented_regular.add(code)
    return print_out(presented_vip, presented_regular)


def print_out(vip, reg):
    print((len(vip_list) + len(regular_list)) - (len(vip)+len(reg)))
    not_presented_vip = vip_list - vip
    not_presented_reg = regular_list - reg
    for v in sorted(not_presented_vip):
        print(v)
    for r in sorted(not_presented_reg):
        print(r)


input_lines(int(input()))
