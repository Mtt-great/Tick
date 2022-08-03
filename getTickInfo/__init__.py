from getTickInfo import getTickInfoBySina as sina
from getTickInfo import getTickInfoByTencent as tencent

if __name__ == "__main__":
    sina.getTickInfoBySina('sh600199')

    tencent.getTickInfoByTencent('sh600199')