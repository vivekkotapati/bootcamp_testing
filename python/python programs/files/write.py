# write()--open an existing file for write operation
# if file already contain some data then it will becoverride
#if file doesn't exists then create a new file
f=open("C:\\Users\\LENOVO\\OneDrive\\Desktop\\out.txt","w")
f.write("vivek upskilling in software\n")
f.write("Attended interview")
f.close()
print("file created successfully")
