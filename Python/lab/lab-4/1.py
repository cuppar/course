try:
    a = input('a = ')
    b = input('b = ')
    result = float(a)/float(b)
    print(result)
except IOError as ioe:
    print(str(ioe))
except ValueError as ve:
    print(str(ve))
except ZeroDivisionError as ze:
    print(str(ze))
except Exception as e:
    print(str(e))
