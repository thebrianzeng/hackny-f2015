import toolz

def pick(whitelist, d):
    return toolz.keyfilter(lambda x: x in whitelist, d)

def exclude(blacklist, d):
    return toolz.keyfilter(lambda x: x not in blacklist, d)
