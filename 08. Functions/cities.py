#8-16. Imports:Using a program you wrote that has one function in it, store that 
#function in a separate file. Import the function into your main program file, and 
#call the function using each of these approaches:
#import module_name
#from module_name import function_name
#from module_name import function_nameas fn
#import module_name as mn
#from module_name import *

#import city_calls

#first one is wrong, using only the first param
#city_calls.describe_city('mexico')
#city_calls.describe_city('mexico','mexico')
#city_calls.describe_city('salvador')
#city_calls.describe_city('rio de janeiro')
#city_calls.describe_city('sao paulo')

#from city_calls import describe_city

#describe_city('mexico')
#describe_city('mexico','mexico')
#describe_city('salvador')
#describe_city('rio de janeiro')
#describe_city('sao paulo')

#from city_calls import describe_city as dc

#dc('mexico')
#dc('mexico','mexico')
#dc('salvador')
#dc('rio de janeiro')
#dc('sao paulo')

#import city_calls as cc

#cc.describe_city('mexico')
#cc.describe_city('mexico','mexico')
#cc.describe_city('salvador')
#cc.describe_city('rio de janeiro')
#cc.describe_city('sao paulo')

from city_calls import *

describe_city('mexico')
describe_city('mexico','mexico')
describe_city('salvador')
describe_city('rio de janeiro')
describe_city('sao paulo')




