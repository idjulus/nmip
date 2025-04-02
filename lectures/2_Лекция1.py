import streamlit as st

menu = st.sidebar.radio('***',
	(
		'Корректная и некорректная задача',
		# 'Практика',
		# 'Пример'
		)
	)

if menu == 'Корректная и некорректная задача':
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

	displayPDF('archive/InverseLecture1.pdf')


if menu == 'Практика':
	r'''
	### Задание 1
	1. C помощью метода конечных разностей решить краевую задачу в $\Omega = [0,1]$ для эллиптического уравнения (1)
	$$
	- \nabla \cdot (k(x) \nabla u) + q(x) u = f(x), \quad x \in [0,1]
	$$
	где
	$
	k(x) = 1, \ q(x) = 0, \ f(x) = 1
	$
	и с граничными условиями

	а) 
	$$
	u(0) = 0, \qquad u(1) = 1
	$$
	б) 
	$$
	u(0) = 0,
	\qquad
	 \frac{\partial u}{\partial n}(1) = 0
	$$
	в)
	$$
	u(0) = 0,
	\qquad
	\frac{\partial u}{\partial n}(1) + u(1) = 0
	$$
	2. Решить задачу (14)-(17) с помощью метода разделения переменных.
	'''


	st.write("")
	st.write("")
	st.write("")

	r"""
	##### Презентация по методу конечных разностей
	"""
	with open("books/fdm.pdf", "rb") as file:
		btn = st.download_button(
			label="скачать МКР",
			data=file,
			file_name="fdm.pdf",
			# mime="image/png",
		)

if menu == 'Пример':
	r'''
	Решается краевая задача Дирихле
	$$
	- \Delta u = 1, \quad x \in [0,1]
	$$
	$$
	u(0) = u(1) = 0
	$$
	'''

	with st.echo():
		import numpy as np
		import matplotlib.pyplot as plt

		# Строим равномерную сетку на отрезке [0,1]
		N = 100                     # кол-во интервалов
		x = np.linspace(0,1,N+1)    # узлы сетки
		h = 1/N                     # шаг сетки

		# Собираем матрицу для внутренних узлов, их кол-во N-1
		A = np.zeros((N-1,N-1))
		for i in range(1,N-2):
			A[i,i] = 2
			A[i,i+1] = -1
			A[i,i-1] = -1
		A[0,0] = 2
		A[0,1] = -1
		A[-1,-1] = 2
		A[-1,-2] = -1
		A /= h**2

		# Правая часть
		f = 1
		b = np.ones(N-1) * f

	st.write('Матрица $A$ и правая часть $b$ без учета граничных условий.')

	c1, c2 = st.columns([1,1])
	# fig_width, fig_height = plt.gcf().get_size_inches()
	# fig1, ax1 = plt.subplots()
	# ax1.set_aspect('equal', adjustable='box')
	# plt.imshow(A)
	# plt.colorbar()
	# c1.pyplot(fig1)
	c1.write('Матрица $A$')
	c1.write(A)

	# fig2, ax2 = plt.subplots()
	# plt.plot(b)
	# c2.pyplot(fig2)
	c2.write('Правая часть $b$')
	c2.write(b)
	
	
	with st.echo(code_location='above'):
		''''''
		# Вектор решения, включая граничные значения
		u = np.zeros(N+1)

		# Учет граничного условия u(0)=u(1)=0
		u0 = 0
		u1 = 0
		u[0] = u0
		u[-1] = u1
		b[0] += u[0]/h**2
		b[-1] += u[-1]/h**2

		# Решение системы Au=b для неизвестных значений решения
		u_ = np.linalg.solve(A, b)

		# Собираем решение
		u[1:-1] = u_

		# Строим график
		fig, ax = plt.subplots()
		plt.plot(x, u)
		#plt.show()

	c1.write('Решение $u$')
	c1.pyplot(fig, use_container_width=False)
