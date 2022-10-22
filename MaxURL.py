from collections import Counter


def TopFiveCommon(urls):
    topfive = []
    for i in range(0, 5):
        most_common,num_most_common = Counter(urls).most_common(1+i)[i]
        topfive.append(most_common)
    return topfive

