def test():
    file = open("/etc/os-release", "r")
    for line in file:
          name, data = line.split('=')
          if name == 'NAME':
              destro = data.strip('"\n')
          if name == 'VERSION':
              ver = data.strip('"\n')

    return (destro, ver)

distribution, version = test()
print ( distribution)
print("\n\n\n")
print(version)
