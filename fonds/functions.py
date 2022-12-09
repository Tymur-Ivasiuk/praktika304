def quotes_slicer(lst, n):
    fin_list = []
    for i in range(0, len(lst), n):
        fin_list.append(lst[i: i+n])
    return fin_list
