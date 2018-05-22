lines = """MemTotal:        7858500 kB
MemFree:          647000 kB
MemAvailable:    2487576 kB
Buffers:          244416 kB"""
memory = []
num = []
memory = lines.split("\n")
for x in range(len(memory)) :
        num = memory[x].split(":")
