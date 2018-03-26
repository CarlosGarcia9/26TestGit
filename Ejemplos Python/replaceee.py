import re
strs = "hola en ingles es $hola$"
print(re.sub(r'{}.*?{}'.format(re.escape("$"),re.escape("$")),"hello",strs))