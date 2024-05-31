#File Extensions
'''
Instruction:
- prompts the user for the name of a file and then 
- outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
    .gif  .jpg  .jpeg  .png  .pdf  .txt  .zip
- If the file’s name ends with some other suffix or has no suffix at all, 
    -output application/octet-stream instead, which is a common default.
'''
#prompt user for filename
filename = input("Filename: ") 

#lowercase the filename for case-insensetivity
file = filename.lower() 

#Splitting to extract the extension/ to access and use parts of strings separated by "."
f, ext = file.split(".") # Eg: cat.jpg >> f = cat, ext = jpg

if file.endswith((".gif", ".jpeg", ".png")):
    print(f"image/{ext}") #Last part is the extension
elif file.endswith((".jpg")):
    print("image/jpeg")
elif file.endswith((".pdf")):
    print("application/pdf")
elif file.endswith((".txt")):
    print("text/plain")
elif file.endswith((".zip")):
    print("application/zip")
else:
    print("application/octet-stream")

'''
if part = file.split(".")
    Example: cat.jpg (given as file)
        part[0] = cat 
        part[1] or part[-1] = jpg

'''