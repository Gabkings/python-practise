def fave_colors(**args):
    for key, val in args.items():
        print('%s favarite color is %s' % (key,val))

x = fave_colors(gab='red',melvin='blue',sam='purple')
print(x)