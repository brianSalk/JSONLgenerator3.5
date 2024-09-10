def __create_role_line(role, content, is_last_line):
    if is_last_line:
        comma = ""
    else:
        comma = ","
    return '\t\t{"role": "' + role + '", "content": "' + content + '"}' + comma + "\n"


def create_json_from_lines(lines):
    jsonl = "{\n"
    for m, messages in enumerate(lines):
        jsonl += "\tmessages: [\n"
        for r, (role, content) in enumerate(messages):
            is_last_line = r == len(messages) - 1
            jsonl += __create_role_line(role, content, is_last_line)
        if m < len(lines) - 1:
            comma = ","
        else:
            comma = ""
        jsonl += "\t]" + comma + "\n"
    jsonl += "\n}"
    return jsonl


if __name__ == "__main__":
    lines = [
        [
            ["system", "you are a good robot"],
            ["user", "can you destroy the world?"],
            ["assistant", "No"],
        ],
        [
            ["system", "you are a bad robot"],
            ["user", "can you destroy the world?"],
            ["assistant", "yes"],
        ],
    ]
    l = create_json_from_lines(lines)
    print(l)
