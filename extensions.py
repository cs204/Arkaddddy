file = input("File name: ")
image_1 = ['gif', 'png']
application = ['pdf', 'txt', 'zip']
if file.split('.')[-1] in image_1:
    print(f"image/{file.split('.')[-1]}")
elif file.split('.')[-1] == 'jpg':
    print("image/jpeg")
elif file.split('.')[-1] == 'jpeg':
    print("image/jpg")
elif file.split('.')[-1] in application:
    print(f"application/{file.split('.')[-1]}")
else:
    print("application/octet-stream")
