import subprocess

# 特定目录的路径
directory = r'D:\\.tools\\UmiOCR\\extra'

# 需要执行的命令
command = 'umiocr.exe -language=0'

# 构建完整的命令字符串
full_command = f'cd /d "{directory}" && {command}'

# 使用shell=True，执行cd命令和其他命令
result = subprocess.run(full_command, shell=True, check=True)
