mySentence = 'loves the color'

color_list = ['red','blue','green','pink','teal','black']

def color_function(name):
    lst = []
    for i in color_list:
        msg = '{} {} {}.'.format(name,mySentence,i)
        lst.append(msg)
    return lst


lst = (color_function('Dane'))
for i in lst:
    print(i)
