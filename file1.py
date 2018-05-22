def test():
    file = open("/proc/cpuinfo", "r")
    line = file.read()
    cpu_core = line.count("processor")
    file.close()
    return (cpu_core)
print(test())

#def get_cpu_cores():
 #   """Get the CPU cores
  #  :param: None
   # :returns: number of CPU cores present"""
   # with open("/proc/cpuinfo") as cpu_file:
  #      cpu_info = cpu_file.read()
  #      return cpu_info.count("processor")
#

#print(get_cpu_cores())
