import streamlit as st

menu = st.sidebar.radio('***',
	(
		'Задание6',
		# 'Пример'
		)
	)

if menu == 'Задание6':
	r'''
	### Задание 6
	
	1. Пусть известно решение $u(x)$, $x\in[0,1]$ начально-краевой задачи
		$$
		\frac{\partial u}{\partial t} - \Delta u = 0, \quad x\in[0,1], \quad t \in [0,0.1]
		$$
		$$
		u(0, t)  = 0,
		\quad
		u(1, t)  = 0, \qquad t \in [0,0.1]
		$$
		с начальным условием
		$$
		u_0(x) = \begin{cases}
		\cfrac{x}{0.3}, & 0 \le x \le 0.3,\\[2ex]
		\cfrac{1-x}{0.7}, & 0.3 < x \le 1,
		\end{cases}
		$$
		

		**Восстановить** функцию $u_0(x)$ при заданном возмущенном решении $u(x,T) = \varphi_\delta(x)$, $x\in[0,1]$, в финальным момент времени $t=0.1$:
		- с помощью итерационного метода минимальных поправок
			$$
			\frac{v_{k+1} - v_{k}}{s_{k+1}} + A v_{k} = \varphi_\delta,
			\qquad \text{где} \quad s_{k+1} = \frac{(A\,r_k, r_k)}{(A\,r_k, A\,r_k)},
			\quad r_k = A\,v_k - \varphi_\delta
			$$
			здесь $A z = u(x, T; z)$ - решение прямой задачи с помощью неявной схемы ($\sigma=1$) с приближенным начальным условием $z$ ($z=v_k,r_k$) в финальный момент времени $T$.

		- c помощью неявного метода простой итерации, $s \le 2$, $(s \approx 1)$
			$$
			B \frac{v_{k+1} - v_{k}}{s} + A v_{k} = \varphi_\delta, \qquad B = E + s \Lambda
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