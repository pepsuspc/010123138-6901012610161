import os 

with open("Test_text.txt","w") as data:
    data.write("Hello Brother")

os.chdir(r"C:\Users\piriy")
print(os.getcwd())
