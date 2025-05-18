def partition(
    line_array: list,
    id_start: int,
    id_stop: int,
) -> list[list[str]]:
    last_id = ""
    partition = []
    result = []
    for line in line_array:
        current_id = line[id_start:id_stop]
        if current_id != last_id and last_id != "":
            result.append(partition)
            partition = []
        partition.append(line)
        last_id = current_id
    if len(partition) > 0:
        result.append(partition)
    return result


def split_lines_by_char(lines: list[str], field_indices: tuple) -> dict:
    result = {}
    start, end = field_indices
    for line in lines:
        key = line[start:end].upper()
        if key not in result:
            result[key] = []
        result[key].append(line)
    return result
