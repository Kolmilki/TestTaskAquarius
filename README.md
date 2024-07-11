*26.06*  
Начал разбиение программы на модули, сделал первый тест. Создал репозиторий на GitHub, а также SSH ключ. Подключил git к
проекту. К концу рабочего дня появился цикличный конфликт. Оставил решение задачи на 27е.  
*27.06*  
Закончил разбиение программы на модули. По неопытности заменил законченную работу на почти не начатую. Разобрался как
делать откат изменений. Сделал merge веток, запушил все в основную. Теперь на сайдовой ветке буду делать тесты с помощью
pytest.
Получил баг, по невнимательности. Заменил две почти идентичные переменные на одну. Решил. Проблема была в том, что
первая переменная содержала строку, а вторая список. В следствие этого в одной из функций итерировался не список с ад-
ресами, а строка  
*28.06*  
Сделал сайд ветку testing_branch и разобрался с pull request. Теперь буду писать тесты.
Встретился с двумя проблемами и оформил их как issue в GitHub. Одну из них в последствие решил - невозможность программы
дотянуться до созданных ею же файлов. Второй issue это полная автоматизация тестирования. При запуске pytest, даже если
это просто модуль, программа запрашивает ввода данных с клавиатуры, чего необходимо избежать при тестировании. Думаю это
решается fixture или ?mock?.  
*01.07*  
Новая рабочая неделя. Закончил черновой вариант тестов. Заменил все абсолютные пути на относительные. Для каждого модуля
теперь есть тесты. Всю программу тестами не покрыл, но сегодня уже виден какой-то результат, так что отправляю пулл ри-
квест на проверку. Из дальнейших рабочих задач осталось полностью автоматизировать тесты (?if main == main?).Ну и конеч-
но правки и дополнения самих тестов.  
*02.07*    
Вынес все функции из конструкции ```if __name__ == "__main__"``` и удалил не нужные фунцкции, которые не несли никакого функ-
ционала. Теперь тестами обладают только те функции, у которых есть внутрянняя логика. Отправил pull request.  
*03.07*  
Начал сравнение linter\`ов. Сравнение идет для linter\`ов, которые проверяют логику программы. Это pylint, ruff и py-
flakes. Pyflakes отказался проверять основную часть программы при любом раскладе. Осталось протестировать ruff.  
*04.07*  
Разобрался с правами для запуска линтеров. Писал статью о сравнении PyLint, Ruff, PyFlake  
*05.07*  
Начал написание shell скриптов для запуска линтеров после коммита. Для этого настроил *git hook* и написал yaml файл, 
который после коммита запускал скрипт, который в свою очередь запускал линтер.  
*08.07*  
Закончил написание двух скриптов, которые запускают проверку в измененных программистом модулях Ruff-ом или Pylint-ом
после коммита. Для этого использовал команду *grep* в связке с командой ```git diff --cached```. Начал написание скрипта,
который првоерял бы только измененные строки.  
*09.07*  
Продолжал писать скрипт для проверки только измененных строк, но прервался на дополнение статьи новым линтером - flake8.
После этого сделал коммит в основную ветку, добавив туда shell скрипты.   
*10.07*  
Начал написание второго этапа статьи где буду рассматривать стилистические линтеры. Написал задачи в виде issue на
GitHub  
*11.07*  
Работаю из дома. Продолжаю писать статью.