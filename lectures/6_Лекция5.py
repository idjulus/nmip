import streamlit as st

menu = st.sidebar.radio('***',
	(
		'Идентификация правой части',
		)
	)

if menu == 'Идентификация правой части':
	import base64
	
	r"""

	"""

	with open("archive/InverseLecture5.pdf", "rb") as file:
		btn = st.download_button(
			label="скачать Лекцию5",
			data=file,
			file_name="InverseLecture5.pdf",
		)

	def displayPDF(file):
		with open(file,"rb") as f:
			base64_pdf = base64.b64encode(f.read()).decode('utf-8')

		# Embedding PDF in HTML
		pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1200" type="application/pdf"></iframe>'
		# pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1200" type="application/pdf">'

		st.markdown(pdf_display, unsafe_allow_html=True)

	displayPDF('archive/InverseLecture5.pdf')
