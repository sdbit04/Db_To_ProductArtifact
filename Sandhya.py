def compare(str1, str2):
    str1_set = set(str1)
    str2_set = set(str2)
    out_1 = ""
    out_2 = ""
    for s in str1:
        if s in str2_set:
            continue
        else:
            out_1 = out_1 + s
    else:
        if out_1 == "":
            out_1 = "<null>"
    for s2 in str2:
        if s2 in str1_set:
            continue
        else:
            out_2 = out_2 + s2
    else:
        if out_2 == "":
            out_2 = "<null>"
    print("str_out_1= {} str_out_2 = {}".format(out_1, out_2))


def filter_out_uniq_comb(comb_list):
    comb_set = set()
    compl_hist = set()
    for comb in comb_list:
        if comb not in compl_hist and comb not in comb_set:
            comb_set.add(comb)
            print(comb)
            comb_items = comb.split(',')
            comb_comp = "{},{}".format(comb_items[1], comb_items[0])
            compl_hist.add(comb_comp)


compare("ABC", "BC")
compare("BC", "BANGALORE")

L1 = ['U1,U2', 'U3,U4', 'U1,U5', 'U2,U1', 'U3,U4']
filter_out_uniq_comb(L1)

