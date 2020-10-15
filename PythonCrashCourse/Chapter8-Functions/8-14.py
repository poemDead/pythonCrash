'''
练习 8-15:打印模型 
将示例 printing_models.py 中的函数放在一个名为 printing_ functions.py 的文件中。
在 printing_models.py 的开头编写一条 import 语句，并修改该文 件以使用导入的函数。
'''
import print_functions as pf

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

pf.print_models(unprinted_designs,completed_models)
pf.show_completed_models(completed_models)