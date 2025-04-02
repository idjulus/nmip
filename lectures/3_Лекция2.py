import streamlit as st

menu = st.sidebar.radio('***',
	(
		'Обратные задачи математической физики',
		)
	)

if menu == 'Обратные задачи математической физики':
	import base64
	
	r"""

	"""

	def displayPDF(file):
		with open(file,"rb") as f:
			base64_pdf = base64.b64encode(f.read()).decode('utf-8')

		# Embedding PDF in HTML
		pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1200" type="application/pdf"></iframe>'
		# pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1200" type="application/pdf">'

		st.markdown(pdf_display, unsafe_allow_html=True)

	displayPDF('../Archive/Lecture2/InverseLecture2.pdf')
