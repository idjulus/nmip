import streamlit as st

menu = st.sidebar.radio('***',
	(
		'Задание4',
		# 'Пример'
		)
	)

if menu == 'Задание4':
	r'''
	### Задание 4
	
	Рассматривается матрица Гильберта как пример плохо обусловленной матрицы
	$$
	A = \begin{bmatrix}
	1 & 1/2 & 1/3 & \ldots\\
	1/2 & 1/3 & 1/4 & \ldots\\
	1/3 & 1/4 & 1/5 & \ldots\\
	\vdots & \vdots & \vdots & \ddots
	\end{bmatrix}
	$$

	Необходимо решить $A x = b$ для матрицы Гильберта размера $n \times n$ и правой части
	$$
	b_i = \sum_{j=1}^n A_{ij}.
	$$
	Для такой задачи точное решение равно $x=[1, 1, \ldots, 1]$.

	Решить систему с зашумленной правой частью
	$$
	b_\delta = b + \delta \sigma,
	$$
	где $\sigma \in N(0,1)$ - случайная величина из стандартного нормального распределения,

	$n=20$, $\delta=0.05$,

	$u_0 = 0$, $\varepsilon = 10^{-6}$,

	$\mathrm{A} = A^TA$, $\mathrm{b}_\delta = A^T b_\delta$

	для этого:

	1. Найти собственные значения матрицы $\mathrm{A}$ для $n=20$.

	2. Использовать метод простой итерации
		$$
		\frac{u^{k+1} - u^{k}}{\tau} + \mathrm{A} u_k = \mathrm{b}_\delta
		$$


	3. Использовать итерационный метод скорейшего спуска
		$$
		\frac{u^{k+1} - u^{k}}{\tau_{k+1}} + \mathrm{A} u_k = \mathrm{b}_\delta
		$$

		$$
		\tau_{k+1} = \frac{(r_k, r_k)}{(\mathrm{A} r_k, r_k)}, \quad r_k = \mathrm{A}u_k - \mathrm{b}_\delta
		$$

	4. Использовать итерационный метод минимальных ошибок
		$$
		\frac{u^{k+1} - u^{k}}{\tau_{k+1}} + \mathrm{A} u_k = \mathrm{b}_\delta
		$$

		$$
		\tau_{k+1} = \frac{(\mathrm{A}r_k, r_k)}{(\mathrm{A} r_k, \mathrm{A}r_k)}, \quad r_k = \mathrm{A}u_k - \mathrm{b}_\delta
		$$
	
	'''


if menu == 'Пример':
	r'''
	Собственные значения матрицы $A$
	'''

	with st.echo():
		import numpy as np
		import scipy as sp
		import matplotlib.pyplot as plt

		N = 20
		A = np.random.rand(N,N)
		U, S, V = np.linalg.svd(A)

		fig, ax = plt.subplots()
		plt.plot(S, 'k-s')
		plt.show()

	st.write(r'Собственные значения $\lambda_k$')
	st.pyplot(fig, use_container_width=True)