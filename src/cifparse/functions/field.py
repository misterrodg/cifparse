def extract_field(
    line: str,
    field_definition: tuple[int, int, callable],
    supplemental_data: str = None,
) -> any:
    start, end, func = field_definition
    field_data = line[start:end]
    if supplemental_data:
        return func(field_data, supplemental_data)
    return func(field_data)
