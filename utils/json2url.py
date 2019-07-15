def JSON2URL(para):
    backStr=''
    for i in para:
        backStr=backStr+i+'='+para[i]+'&'
    return backStr[:-1]
