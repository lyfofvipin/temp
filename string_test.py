teasting_string = "Teasting  in our code \
yes it is working "
print teasting_string
print "$"*50
teasting_string = "my name is vipin \n i live in alwar"
print teasting_string
print "$"*50
teasting_string = """ Here we are
going to
write a
lotes of
line in
our code
for testing"""
print teasting_string
print "$"*50
print teasting_string.title()
print "$"*50
print teasting_string.lower()
print "$"*50
print teasting_string.upper()
print "$"*50
teasting_string = """ Here we are
gOiNg tO
wRite a
loTes of
line iN
our coDe
for teSting"""
print teasting_string.swapcase()
print "$"*50
teasting_string = "Here we are gOiNg tO use isalnum()"
print teasting_string.isalnum()
print "$"*50
teasting_string = "HerewearegOiNgtOuseisalnum()"
print teasting_string.isalnum()
print "$"*50
teasting_string = "HerewearegOiNgtOuseisalnum"
print teasting_string.isalnum()
print "$"*50
teasting_string = "12345"
print teasting_string.isdigit()
print "$"*50
teasting_string = "Is Title Or Not"
print teasting_string.istitle()
print "$"*50
teasting_string = "is lower or not"
print teasting_string.islower()
print "$"*50
teasting_string = "IS LOWER OR NOT"
print teasting_string.isupper()
print "$"*50
teasting_string = "Now we are going to split string into list"
print teasting_string.split(" ")
print "$"*50
# or
teasting_list = teasting_string.split(" ")
print teasting_list
print "$"*50
print "==".join("Now-we-are-going-to-use-join-into-string".split("-"))
print "$"*50
# or
teasting_string = "==".join("Now-we-are-going-to-use-join-into-string".split("-"))
print teasting_string
print "$"*50
teasting_string = "Now.we.are.going.to.learn.striping"
print teasting_string.lstrip("cwsd.")
print "$"*50
# find
print teasting_string.find("learn")
print "$"*50
print teasting_string.endswith("ing")
print "$"*50
print teasting_string.startswith("No")
print "$"*50
print teasting_string.startswith("no")
print "$"*50
