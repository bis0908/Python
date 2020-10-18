def plus(*args, **kwargs): #args: for positional arguments. ex; 12,5,7,8
    result = 0              # kwargs: keyword arguments. ex; name="something"
    for number in args:
        result += number
    print(result)
    

plus(189,7,951,98,7,981,9,87,951,21,2,1456,4,51,21,21,5,4,78,652,1)
