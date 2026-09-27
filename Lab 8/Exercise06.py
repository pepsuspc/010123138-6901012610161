import os

print(os.getcwd())
folder = input("Enter directory: ")

total_size = 0
count = 0

for name in os.listdir(folder):
    path = os.path.join(folder,name)
    if os.path.isfile(path):
        size = os.path.getsize(path)
        print(f"{name:40} {size:>12,} bytes")
        total_size += size
        count += 1

print("-" * 59)
print(f"{count} files, total size = {total_size:,} bytes ({total_size / 1024:.2f} KB)")