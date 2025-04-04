import streamlit as st

menu = st.sidebar.radio('***',
	(
		'Метод регуляризации Тихонова',
		)
	)

if menu == 'Метод регуляризации Тихонова':
	import base64
	
	r"""

	"""

	with open("archive/InverseLecture3.pdf", "rb") as file:
		btn = st.download_button(
			label="скачать Лекцию3",
			data=file,
			file_name="InverseLecture3.pdf",
		)

	def displayPDF(file):
		with open(file,"rb") as f:
			base64_pdf = base64.b64encode(f.read()).decode('utf-8')

		# Embedding PDF in HTML
		pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1200" type="application/pdf"></iframe>'
		# pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1200" type="application/pdf">'

		st.markdown(pdf_display, unsafe_allow_html=True)

	displayPDF('archive/InverseLecture3.pdf')
