def write_file(file_name, file_content):
    file_name=f"{file_name}.txt"
    with open(file_name, mode='w') as f:
        f.write(file_content)
    

def append_file(file_name, append_content):
    file_name = f"{file_name}.txt"
    with open(file_name, mode="a") as f:
        f.write(append_content)

def read_file(file_name):
    file_name =f"{file_name}.txt"
    with open(file_name, mode="r") as f:
        return f.read()