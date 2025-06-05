# Harvard exercise number 3

'''
prompt user for a file name with extension and return the type of file and extension
ex: happy.png = image/PNG
'''

# User Prompt

f = input("File Name: ")

# Sort file types

f = f.lower()
ft = f[-4:]

# IMAGES
if ft == ".png":
    print("Image/png")
elif ft == ".jpg":
    print("Image/jpeg")
elif ft == ".gif":
    print("Image/gif")
elif ft == ".zip":
    print("Application/zip")
elif ft == ".pdf":
    print("Application/pdf")
elif ft == ".txt":
    print("Text/plain")
else:
    print("application/octet-stream")


#Optmized Code
'''
# Prompt user
filename = input("File Name: ").strip().lower()

# Define MIME types
mime_types = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Extract extension
import os
_, ext = os.path.splitext(filename)

# Get and print the MIME type
print(mime_types.get(ext, "application/octet-stream"))
'''

