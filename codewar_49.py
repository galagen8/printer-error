"""
In a factory a printer prints labels for boxes. 
For one kind of boxes the printer has to use colors which, 
for the sake of simplicity, are named with letters from a to m.

s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"


"""

s = 'wewe'

def printer_error(s):
    error = 0
    for x in s:
        if ord(x) > 109:
            error += 1
    color = len(s)
    return f'{color}/{error}'

print(printer_error(s))