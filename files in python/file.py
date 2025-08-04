# file=open("text_doc.txt","r")
# print(file.read())
# file.close()

# file=open("text_doc.txt","w")
# file.write("File Handling")
# file.close()

# file=open("text_doc.txt","a")
# file.write("File Handling")
# file.close()

# with open("text_doc.txt","a") as file:
#     file.write("File Handling")

with open("text_doc.txt", "a") as file:
    file.write("File Handling\n")  # adds a newline after each append



