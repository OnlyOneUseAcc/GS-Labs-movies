# GS-Labs-movies

[Презентация о проделанной работе](https://prezi.com/view/DEcFlasium9DMIARp87Z/)

# Информация по репозиторию
### [Ссылка на данные](https://drive.google.com/drive/folders/1zJzgitzK-oSi_Zgz01_cPaq4g1QnrwAS?usp=sharing)

## Описание таблиц

### Исходные данные до обоработки (Папка raw)

**content.csv:** Полное описание фильмов
 
 **missed_movies.csv:** Информация о длительности фильмов, у которых она пропущена в content.csv

**USER_UID.csv:** UID пользователей для рекомендации фильмов (Данные для предсказания)

**watch_history.csv:** Полная история просмотренного контента для каждого пользователя

### Обработанные или вспомогательные данные (Папка postprocessing)

**content.csv:** Полное описание фильмов с заполненными пропусками и объединением эпизодов в сериалы

**film_genres.csv:** Таблица принадлежности фильма к жанрам

**sparse_matrix.npz:** Разреженная матрица формата lil вида: Пользователь:Фильм -> временная доля просмотра пользователем относительно длительности фильма

**user_content_types.csv:** Время просмотра пользователем каждого из типа контента

**users_genres.csv**: Время просмотра пользователем каждого из жанра

**watch_history.csv:** Полная история просмотренного контента для каждого пользователя с учетом изменений в таблице content.csv

## Визуальное описание исходных данных

- Распределение по типам
![alt text](/data/plots/type_bar.png) 
   
 - После обработки пропущенных типов
![alt text](/data/plots/post_missed_types.png) 
   
- Количество пропущенных типов
![alt text](/data/plots/missed_types.png)


## Отображение списка рекомендованных фильмов для 76321

![alt text](https://github.com/julesadikhanyan/cinema/blob/master/img/2.JPG)


![alt text](https://github.com/julesadikhanyan/cinema/blob/master/img/3.JPG)


![alt text](https://github.com/julesadikhanyan/cinema/blob/master/img/4.JPG)

