import streamlit as st

menu = st.sidebar.radio('***',
	(
		'Задание5',
		# 'Пример'
		)
	)

if menu == 'Задание5':
	r'''
	### Задание 5
	
	1. Пусть известно решение $u(x)$, $x\in[0,1]$ краевой задачи
		$$
		-\Delta u = f(x), \quad x\in[0,1],
		$$
		$$
		u(0)  = 0,
		\qquad
		u(1)  = 0
		$$

		Точная правая часть имеет вид
		$$
		f(x) = \begin{cases}
		0, & 0 \le x \le 0.5,\\
		1, & 0.5 < x \le 1,
		\end{cases}
		$$
		

		**Определить** функцию $f(x)$ при заданном возмущенном решении $u_\delta(x)$, $x\in[0,1]$:
		- с помощью метода регуляризации Тихонова через уравнение Эйлера
			$$
			(E + \alpha D^* D) f_\alpha = D u_\delta
			$$
		- с помощью метода простой итерации
			$$
			D \frac{f_{k+1} - f_{k}}{\tau} + f_{k} = D u_\delta
			$$

	2. (:star::star:) Пусть известно решение $u(x,t)$ начально-краевой задачи, $l=1, T=1$,
		$$
		\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2} + f(x,t),
		$$
		$$
		u(0,t) = 0, \quad u(l,t) = 0, \quad 0 < t \le T,
		$$
		$$
		u(x,0)= 0, \quad 0 \le x \le l.
		$$

		Точная правая часть имеет вид
		$$
		f(x,t) = 10 t (1-t)x(1-x).
		$$
		
		Уровень зашумления $\delta=0.001$. Найти правую часть итерационным методом.
		$$
		\frac{f_{k+1} - f_{k}}{\tau_{k+1}} + \mathcal{G}^*\mathcal{G} f_k = \mathcal{G^*} u_\delta
		$$
		
		$$
		\tau_{k+1} = \frac{\|r_k\|^*}{\|\mathcal{G}r_k\|^*}, \qquad \text{где} \quad r_k = \mathcal{G}^*\mathcal{G}f_k - \mathcal{G}^*u_\delta
		$$

		$
		y_\delta = \mathcal{G^*} u_\delta
		$

		$
		v = \mathcal{G}f_k
		$
		есть решение прямой задачи
		$$
		\begin{aligned}
		\frac{\partial v}{\partial t} - \frac{\partial^2 v}{\partial x^2} &= f_k(x,t), \\
		v(0,t) = 0, \quad v(l,t) &= 0, \quad 0 < t \le T,\\
		v(x,0) &= 0, \quad 0 \le x \le l.
		\end{aligned}
		$$

		$
		w = \mathcal{G^*} v
		$
		есть решение прямой задачи
		$$
		\begin{aligned}
		- \frac{\partial w}{\partial t} - \frac{\partial^2 w}{\partial x^2} &= v(x,t), \\
		w(0,t) = 0, \quad w(l,t) &= 0, \quad 0 < t \le T,\\
		w(x,T) &= 0, \quad 0 \le x \le l,
		\end{aligned}
		$$

		$r_k = w - y_\delta$.

		$\mathcal{G} r_k$ есть решение аналогичной прямой задачи.

		---
		1. Найти точное решение $u(x,t)$ при заданной правой части, добавить шум;
		2. Найти решение $y_\delta(x,t)$ сопряженной задачи с правой частью $u_\delta$;
		3. Начальное приближение $k=0$, $f_k = 0$;
		4. Найти решение $v(x,t)$ прямой задачи с правой частью $f_k$;
		5. Найти решение $w(x,t)$ сопряженной задачи с правой частью $v$;
		6. Найти решение прямой задачи с правой частью $r_k := w - y_\delta$ (невязка);
		7. Найти итерационный шаг $\tau_{k+1} = \|r_k\|^* / \|\mathcal{G}r_k\|^*$.
		8. Обновить приближение $f_{k+1} = f_k - \tau_{k+1} r_k$;
		9. Проверить условие сходимости $\|v - u_\delta\|^* \le \delta$, если выполнено остановить, иначе $k:= k + 1$, перейти к шагу 4.
		
		---

		p.s.: Реализовать программный код `PROBLEM6` из книги Самариского А.А., Вабищевича П.Н., стр. 241, переписав в Python.
	
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