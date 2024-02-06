InString = input("File Name: ").strip().lower()
exten = InString[-4:]

if exten == '.gif':
    print('image/gif')
elif exten == '.jpg' or InString[-5:] == '.jpeg':
    print('image/jpeg')
elif exten == '.png':
    print('image/png')
elif exten == '.pdf':
    print('application/pdf')
elif exten == '.txt':
    print('text/plain')
elif exten == '.zip':
    print('application/zip')
else:
    print('application/octet-stream')