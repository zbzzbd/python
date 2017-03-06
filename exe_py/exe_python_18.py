import os
print os.path.dirname(os.sep)
root_dir=os.path.dirname(os.path.abspath(__file__))
print root_dir

for item in os.listdir(root_dir):
    if  item.endswith('.txt'):
        print item.capitalize()
