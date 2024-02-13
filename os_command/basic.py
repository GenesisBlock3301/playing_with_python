import subprocess

def interact_with_command(command, inputs):
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )

    stdout, stderr = process.communicate(input=inputs)

    return process.returncode, stdout, stderr

# Example command that prompts for input
command = ['cat']

# Example inputs as if you were typing them
inputs = "Hello\nWorld\n"

return_code, stdout, stderr = interact_with_command(command, inputs)

print("Return code:", return_code)
print("Standard output:")
print(stdout)
print("Standard error:")
print(stderr)
