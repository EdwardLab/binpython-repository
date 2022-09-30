print("""
BINPython software source switch
1.Offical Github
2.BINPython Offical US Server []
""")
num = input('Enter a sequence number to switch sources (eg "1"):')
if num == "1":
    f = open(runpath + f"/binpython_files/apps/source.config", "w")
    f.write("https://raw.githubusercontent.com/xingyujie/binpython-repository/main/")
    print("Done!")
if num == "2":
    f = open(runpath + f"/binpython_files/apps/source.config", "w")
    f.write("http://154.12.37.151:7800/")
    print("Done!")
else:
    print('Please enter the correct number (eg "1")')