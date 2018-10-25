#example of keyword arguments
def grocery(item,price):
    print('Item=%s' % item)
    print('Price =%.2f' %price)

#call grocery() and pass 2 arguments
grocery(price=88.0, item='Oil')
grocery(item='Sugar',price=100.0)
