import subprocess

def run_c_code(file_name):
    compile_cmd = f"gcc {file_name} -o output"
    run_cmd = "./output"
    try:
        subprocess.run(compile_cmd, check=True, shell=True)
        result = subprocess.run(run_cmd, check=True, shell=True, capture_output=True)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print("Compilation or execution failed:", e)

file_name = "main.c"
run_c_code(file_name)

