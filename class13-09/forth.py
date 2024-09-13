checkstr ="""Hello user this is your First page. 
Make sure that you have done your research and study done before proceed."""

# def UpperConverter(checkstr):
#     checkstr = checkstr.upper()
#     return checkstr

UpperConverter = lambda checkstr: checkstr.upper()
print(UpperConverter(checkstr))