def find(my_dict,fun):
    for key, value in my_dict.items():
        if(fun(key)):
            return value
    return None

def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    roles= mapping["roles"]
    categories=mapping["categories"]
    categoryIdsSorted=mapping["categoryIdsSorted"]
    # put your code here
    result = {}
    result["categories"] = []
    for idcat in categoryIdsSorted:
        result_find_cat = find(categories,lambda item: idcat==item)  
        role_ids = result_find_cat["roleIds"]
        list_result_find_role = []
        for idrole in role_ids:
            find_role = find(roles,lambda item: idrole==item)
            list_result_find_role.append({"id":find_role["id"],"text":find_role["name"]})
        result["categories"].append(
            {"id":"category-"+idcat,
             "text":result_find_cat["name"],
             "items":list_result_find_role}
            )
    return  result
