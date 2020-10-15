'''
8-15 各种import方法尝试
import module_name
from module_name import function_name
from module_name import function_name as fn 
import module_name as mn
from module_name import *
'''
from print_functions import print_models as pm


unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

# print_functions.print_models(unprinted_designs,completed_models)
# print_functions.show_completed_models(completed_models)
pm(unprinted_designs,completed_models)

