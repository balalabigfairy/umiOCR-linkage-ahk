import subprocess

# 特定目录的路径
directory = r'D:\\.tools\\UmiOCR\\extra'

# 需要执行的命令
command = 'umiocr.exe -screenshot'

# 构建完整的命令字符串
full_command = f'cd /d "{directory}" && {command}'

# 使用shell=True，执行cd命令和其他命令
result = subprocess.run(full_command, shell=True, check=True)

# 检查命令是否成功执行
if result.returncode == 0:
    print('命令执行成功')
else:
    print('命令执行失败')
