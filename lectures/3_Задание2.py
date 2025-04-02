import streamlit as st

menu = st.sidebar.radio('***',
	(
		'Задание2',
		'Пример'
		)
	)

if menu == 'Задание2':
	r'''
	### Задание 2
	
	1. C помощью __неявной схемы__ решить начально-краевую задачу в $\Omega = [0,1]$ для параболического уравнения
		$$
		\frac{\partial u}{\partial t} - \nabla \cdot (k(x) \nabla u) + q(x) u = f(x), \quad x \in [0,1], \quad 0 < t \le 1,
		$$
		где
		$\
		k(x) = 1, \ q(x) = 0.1, \ f(x) = 1,
		$

		с начальным условием $\ u(x,0) = 0, \quad x \in [0,1]$

		и с граничными условиями:

		- $\displaystyle u(0, t) = 0, \qquad u(1, t) = 1, \quad 0 < t \le 1$

		- $\displaystyle u(0, t) = 0, \qquad \frac{\partial u}{\partial n}(1,t) + u(1,t) = t, \quad 0 < t \le 1$        (:star:)
	
	2. Построить график:

		- решения в финальный момент времени, $u(x,T), \ T = 1$.

		- решения в внутренней точке $u(x^*, t)$, $x^* = 0.5$.
	
	'''


if menu == 'Пример':
	r'''
	Решается начально-краевая задача для параболического уравнения
	$$
	u_t - \Delta u = 0, \quad x \in [0,1], \quad 0 < t \le T,
	$$
	$$
	u(x, 0) = 1,
	$$
	$$
	u(0,t) = 1, \quad u(1,t) = 0.
	$$
	'''

	with st.echo():
		import numpy as np
		import matplotlib.pyplot as plt

		# Строим равномерную сетку на отрезке [0,1]
		l = 1.0
		N = 20                      # кол-во интервалов
		x = np.linspace(0,l,N+1)    # узлы сетки
		h = 1/N                     # шаг сетки

		# Сетка по времени
		T = 0.1
		M = 100
		t = np.linspace(0,T,M+1)
		tau = T/M

		print(tau/h**2)             # для явной схемы < 0.5 

		# Условия задачи
		f = 0.0
		u0 = np.ones_like(x)
		mu0 = 1.0
		mu1 = 0.0

		# Решение в текущий момент времени
		u = u0.copy()

		# Решение на следующий временной слой
		u_hat = np.zeros_like(x)

		fig, ax = plt.subplots()

		# Явная схема
		for s in range(1,M+1):
			for i in range(1,N):
				u_hat[i] = u[i] + tau/h**2 * (u[i-1] - 2*u[i] + u[i+1]) + tau*f
			u_hat[0] = mu0
			u_hat[-1] = mu1
			u = u_hat.copy()

			if s % 10 == 0:
				plt.plot(x, u_hat, label=fr'$t={t[s]}$')

		plt.legend()
		plt.show()

	st.write('Решение $u(x,t)$')
	st.pyplot(fig, use_container_width=True)