def translate_sql_types(type_val: str) -> str:
    if type_val == "str":
        return "TEXT"
    if type_val == "int":
        return "INTEGER"
    if type_val == "bool":
        return "INTEGER"
    if type_val == "float":
        return "REAL"
    return "TEXT"
