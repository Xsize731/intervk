Целью задания было классифицировать временные ряды.В train выборке было 80 тысяч рядов, я не смог их визуализировать и поэтому визуализировал данные, которые смог выделить из train выборки. Я выделил такие признаки как: среднее, дисперсию, среднеквадратичное отклонение, минимальное и максимальное значение, ассиметрию и эксцесc, а также построил распределение целевой переменной.<br />
Целевая перменная:<br />
![image](https://github.com/user-attachments/assets/e21e9ea1-24d1-4865-9796-5c3f29139d02)<br />
Предложим гипотезу о том, что статистические данные различны для класса 0 и 1. Построим их гистограммы и посмотрим на них.<br />
![image](https://github.com/user-attachments/assets/e72e03df-4848-4c25-8a85-e2b84b5c5fe2)
![image](https://github.com/user-attachments/assets/ec9d4e4b-b987-41f5-b12e-7c457f7594f5)
![image](https://github.com/user-attachments/assets/e4d51b5a-9f96-4b2b-9bb1-2d05a8f5e972)
![image](https://github.com/user-attachments/assets/2fd8db1b-2e69-425f-b313-2e5374c8e921)
![image](https://github.com/user-attachments/assets/3810e29e-8900-489b-a3fa-976f983510ec)
![image](https://github.com/user-attachments/assets/5c3b5df9-9668-40a7-b4fc-7a98f444be05)
![image](https://github.com/user-attachments/assets/9f74ff38-7949-40b4-a7ac-f8882e8b917e)<br />
Можно заметить, что самая большая разница для среднеквадратичного отклонения, хотя небольшие различия есть и для других признаков.
Далее провел нормализацию признаков, подобрал гипемараметры и обучил случайный лес.<br /> 
Точность по метрике roc_auc получилась 76%.





