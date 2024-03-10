
def show_completed_models (completed_models:list[str]):
    """Prints all items in completed_models"""
    for model in completed_models:
        print(model.upper())

def print_models(unprinted_designs:list, completed_models:list):
    """Adds unprinted_desings to completed_models"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    return completed_models.sort()

