import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)

        abs_file_path = os.path.abspath(
            os.path.join(abs_working_dir, file_path)
        )

        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" outside working directory.'

        parent_dir = os.path.dirname(abs_file_path)
        os.makedirs(parent_dir, exist_ok=True)

        with open(abs_file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f'Success: File "{file_path}" written.'

    except PermissionError:
        return f'Error: Permission denied for "{file_path}".'
    except Exception as e:
        return f"Error: {str(e)}"