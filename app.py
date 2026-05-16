import streamlit as st
import qrcode
from io import BytesIO
st.set_page_config(
	page_title="QR Code Generator",
	page_icon="🔳",
	layout="centered"
)
st.title("QR Code Generator")
st.write("Create a custom QR code for any link and download it as a PNG image.")
st.divider()

st.sidebar.title("QR Setting")
st.sidebar.write("Customize your QR code here.")

url=st.text_input("Enter the URL")
file_name=st.text_input("Enter file name", "my_qr_code")

qr_colour_options = {
    "AEVUM Black": "#111111",
    "Deep Blue": "#0B1F3A",
    "Muted Gold": "#C8A96A",
    "Dark Green": "#1F3D2B"
}

qr_colour_name = st.sidebar.selectbox(
    "Choose QR colour",
    list(qr_colour_options.keys())
)

qr_colour = qr_colour_options[qr_colour_name]

bg_colour_options = {
    "Warm Ivory": "#F5F1E8",
    "Clean White": "#FFFFFF",
    "Soft Grey": "#EAEAEA"
}

bg_colour_name = st.sidebar.selectbox(
    "Choose background colour",
    list(bg_colour_options.keys())
)

bg_colour = bg_colour_options[bg_colour_name]

qr_size=st.sidebar.selectbox(
	"Choose QR size",
	['Small', 'Medium', 'Large']
)

st.sidebar.markdown("""
**Tip:** Use a dark QR colour with a light background for better scanning.

**Developer's suggestion:**
- QR colour: AEVUM Black
- Background colour: Warm Ivory
- Size: Medium
""")

if qr_size=='Small':
	box_size=6
elif qr_size=='Medium':
	box_size=10
else:
	box_size=14
generate_button=st.button("Generate QR Code")

if generate_button:
	if url.strip() =='':
		st.warning("Please enter a URL first.")
	elif file_name.strip() =='':
		st.warning("Please enter a file name.")
		
	else:
		qr=qrcode.QRCode(
			version=1,
			box_size=box_size,
			border=4
		)
		qr.add_data(url)
		qr.make(fit=True)
		img=qr.make_image(fill_color=qr_colour, back_color=bg_colour)
		
		pil_img=img.get_image()
		
		st.image(pil_img, caption="Your QR Code")
		
		st.success("QR code generated successfully!")
		st.write('File ready:', file_name.strip() + ".png")
		
		buffer=BytesIO()
		pil_img.save(buffer, format='PNG')

		st.download_button(
			label="Download QR Code",
			data=buffer.getvalue(),
			file_name=file_name.strip() +'.png',
			mime='image/png'
		)
		
st.write("You entered:", url)