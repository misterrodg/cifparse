def extract_field(
    line: str, field_definition: tuple[int, int, callable], type: str = None
) -> any:
    start, end, func = field_definition
    field_data = line[start:end]
    if type:
        return func(field_data, type)
    return func(field_data)
