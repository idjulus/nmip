import streamlit as st

menu = st.sidebar.radio('***',
	(
		'Задание7',
		# 'Пример'
		)
	)

if menu == 'Задание7':
	r'''
	### Задание 7
	
	1. Пусть $u(x)$, $x\in[0,1]$, есть решение начально-краевой задачи, $T=1$,
		$$
		\frac{\partial u}{\partial t} - \Delta u = 0, \quad x\in[0,1], \quad t \in [0,T]
		$$
		с граничным условием Неймана (слева) и Дирихле (справа)
		$$
		-k(x)\frac{\partial u}{\partial x}(0, t) = 0, \quad 0 < t \le T,
		$$
		$$
		u(1, t) = \psi(t), \qquad t \in [0,T]
		$$
		и с начальным условием
		$$
		u_0(x) = 0.
		$$

		Дополнительная информация (граничное условие Дирихле на левом конце)
		$$
		u(0,t) = \varphi(t), \qquad t \in [0,T]
		$$
		

		Необходимо **восстановить** функцию $\psi(t)$ при заданном возмущенном граничном условии слева
		$u(0,t) = \varphi_\delta(x)$, $t\in[0,T]$
		**с помощью метода возмущения нелокального граничного условия**.


		Рассматривается сеточная задача c нелокальным граничным условием как регуляризация обратной задачи, $A u = \frac{\partial}{\partial x}(k(x)\frac{\partial u}{\partial x})$,
		$$
		\frac{u_\alpha^{n+1} - u_\alpha^n}{\tau} + A u_\alpha^{n+1} = 0,
		$$ 
		$$
		k(x)\frac{\partial u_\alpha^n}{\partial x}(0) = 0,
		$$
		$$
		u_\alpha^n(0) + \alpha u_\alpha^n(l) = \varphi^n
		$$
		$$
		u_\alpha(x,0) = 0
		$$
		Решение на новом временном слое $t_{n+1} = (n+1) \tau$ ищется в виде
		$$
		u_\alpha^{n+1}(x) = z^{n+1}(x) + q(x) v^{n+1}.
		$$
		Здесь $v^{n+1}$ приближает значение функции $\psi(t)$ в точке $t=t_{n+1}$.

		Функция $z^{n+1}(x)$ находится из решения
		$$
		\frac{z^{n+1} - u^n_\alpha}{\tau} + A z^{n+1} = 0,
		$$
		$$
		k(x)\frac{\partial z^n}{\partial x}(0) = 0,
		$$
		$$
		z^{n+1}(l) = 0
		$$
		$$
		z^0(x) = 0.
		$$
		Функция $q(x)$ находится из решения
		$$
		\frac{q}{\tau} + A q = 0,
		$$
		$$
		k(x)\frac{\partial q}{\partial x}(0) = 0,
		$$
		$$
		q(l) = 1.
		$$
		Тогда решение обратной задачи выражается через формулу
		$$
		v^{n+1} = \frac{\varphi^{n+1} - z_0^{n+1}}{\alpha + q_0}
		$$


		Далее в примере точное значение граничного условия справа берется
		$$
		\psi(t) = \begin{cases}
		\cfrac{2t}{T}, & 0 < t \le \cfrac{T}{2}, \\[2ex]
		\cfrac{2(T-t)}{T}, & \cfrac{T}{2} < t \le T.
		\end{cases}
		$$

		Выполнить следующие шаги:

		1. Решить прямую задачу с точным граничным условием справа;
		2. Вычислить $\varphi(t) = u(0,t)$, добавить шум, $\varphi_\delta(t)$, $\delta=0.005$;
		3. Найти $q(x)$;
		4. Решить задачу для $z(x, t)$, параллельно восстанавливая $v(t)$;
		5. Построить график $v(t)$ и точное $\psi(t)$.

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