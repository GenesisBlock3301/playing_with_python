import subprocess


def execute_shell_command(command=None, password=None):
    if password:
        command = f'echo "{password}" | sudo -S {command}'
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, universal_newlines=True)
    while True:
        # Read stdout and stderr line by line
        line_stdout = process.stdout.readline().strip()
        line_stderr = process.stderr.readline().strip()

        # Print stdout and stderr lines
        if line_stdout:
            print("output:", line_stdout)
        if line_stderr:
            print("error:", line_stderr)

        # If subprocess finished, break the loop
        if not line_stdout and not line_stderr:
            break


# Example usage:
execute_shell_command(command="sudo apt -y autoremove", password='bs23')
