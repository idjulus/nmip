import streamlit as st

menu = st.sidebar.radio('***',
	(
		'Задание3',
		'Пример'
		)
	)

if menu == 'Задание3':
	r'''
	### Задание 3
	
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
	b_i = \sum_{j=1}^n A_{ij},
	$$
	при этом точное решение равно $x=[1, 1, \ldots, 1]$.

	1. Найти собственные значения матрицы $A$ для $n=10, 20, 100$.

	2. Решить систему с зашумленной правой частью
		$$
		b_\delta = b + \delta \sigma,
		$$
		где $\sigma \in N(0,1)$ - случайная величина из стандартного нормального распределения.

		$n=20$, $\delta=0.05$

	3. Решить систему с помощью регуляризации Тихонова
		$$
		J(x) = \|Ax - b_\delta\|^2 + \alpha \|x\|^2 \longrightarrow \min_x
		$$
		которая сводится к решению уравнения Эйлера
		$$
		(A^T A + \alpha E) x = A^T b_\delta
		$$
		$E$ - единичная матрица.

		Исследовать различные значения $\alpha \in [10^{-8}, 10^{-2}]$. Пусть $x_\alpha$ найденное решение

		- построить график $J(x_\alpha)$ от $\alpha$;
		
		- построить график $\|Ax_\alpha - b_\delta\|^2$ от $\alpha$;
		
		- построить график $\alpha\|x_\alpha\|^2$ от $\alpha$.
	
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