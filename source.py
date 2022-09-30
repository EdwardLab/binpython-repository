print("""
BINPython software source switch
1.Offical Github
2.BINPython Offical US Server

***GitHub restricts large files and prevents abuse, so except for GitHub sources ("1" number), all support large files and third-party packages, we recommend switching non-GitHub sources
""")
num = input('Enter a sequence number to switch sources (eg "1"):')
if num == "1":
    f = open(runpath + f"binpython_files/apps/source.config", "w")
    f.write("https://raw.githubusercontent.com/xingyujie/binpython-repository/main/")
    print("Done!")
if num == "2":
    f = open(runpath + f"binpython_files/apps/source.config", "w")
    f.write("http://repo.binpython.org/")
    print("Done!")
else:
    print('Please enter the correct number (eg "1")')
