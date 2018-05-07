from GA.Utils import Info



def svg(sn):
    """
    functia a fost luata de la : https://github.com/brianpursley/sorting-network/blob/master/sortingnetwork.py
    ??? drepturile de autor. este MIT
    """
    scale = 1
    xscale = scale * 35
    yscale = scale * 20

    innerResult = ''
    x = xscale
    usedInputs = []
    for c in sn.get_comparators():
        if c[0] in usedInputs or c[1] in usedInputs:
            x += xscale
            del usedInputs[:]
        for ui in usedInputs:
            if (ui > c[0] and ui < c[1]) or (ui > c[1] and ui < c[0]):
                x += xscale / 3
                break
        y0 = yscale + c[0] * yscale
        y1 = yscale + c[1] * yscale
        innerResult += "<circle cx='%s' cy='%s' r='%s' style='stroke:black;stroke-width:1;fill=yellow' />" % (
            x, y0, 3)
        innerResult += "<line x1='%s' y1='%s' x2='%s' y2='%s' style='stroke:black;stroke-width:%s' />" % (
            x, y0, x, y1, 1)
        innerResult += "<circle cx='%s' cy='%s' r='%s' style='stroke:black;stroke-width:1;fill=yellow' />" % (
            x, y1, 3)
        usedInputs.append(c[0])
        usedInputs.append(c[1])

    w = x + xscale
    n = Info.NR_WIRES
    h = (n + 1) * yscale
    result = "<?xml version='1.0' encoding='utf-8'?>"
    result += "<!DOCTYPE svg>"
    result += "<svg width='%spx' height='%spx' xmlns='http://www.w3.org/2000/svg'>" % (w, h)
    for i in range(0, n):
        y = yscale + i * yscale
        result += "<line x1='%s' y1='%s' x2='%s' y2='%s' style='stroke:black;stroke-width:%s' />" % (0, y, w, y, 1)
    result += innerResult
    result += "</svg>"
    with open('sorting_network.svg', 'w') as file:
        file.write(result)
