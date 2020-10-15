def print_models(unprinted_designs, completed_models):
    """弹出未完成列表的项，打印，并添加进完成列表。"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model:{current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """打印所有完成列表的项"""
    print("\nThe following models have been printed: ")
    for model in completed_models:
        print(model)