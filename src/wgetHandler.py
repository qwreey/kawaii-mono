from .wget import wget
import math

# bar 를 커스텀.... 하는 어떤 글에서 가져온거
def bar_custom(current, total, width=80):
    width=30
    avail_dots = width-2
    shaded_dots = int(math.floor(float(current) / total * avail_dots))
    percent_bar = '[' + '■'*shaded_dots + ' '*(avail_dots-shaded_dots) + ']'
    progress = "%d%% %s [%d / %d]" % (current / total * 100, percent_bar, current, total)
    return progress

# 그냥 간단한 download 함수인데 좀 프린트를 넣어봤는거?
def download(url, fileName):
    print("Downloading resource to "+fileName+" ...")
    wget.download(url, fileName, bar=bar_custom)
    print(" [OK]")
