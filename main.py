import qrcode
url=input("Enter the url:").strip()
while url=='':
	print('URL cannot be empty. Please enter a vaild URL.')
	url=input('Enter the url:').strip()
filename= input("Enter file name:")
while filename=='':
	print('FileName cannot be empty. Please enter a vaild FileName.')
	filename=input('Enter the filename:').strip()
print("You entered", url)
qr=qrcode.QRCode(
	version=1,
	box_size=20,
	border=4
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="darkblue", back_color="white")
img.save(filename+'.png')
print("QR code successfully saved as:", filename+'.png')