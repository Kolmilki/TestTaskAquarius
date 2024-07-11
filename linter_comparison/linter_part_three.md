# Методические указания для проверок линтерами
Здесь собраны наборы пакетов для проверки кода на разных этапах разработки.  

## **Этапы:**
* Перед git commit - здесь необходим пакет документов, который покажет серьезные логические ошибки и проведет
форматирование кода к стандарту pep8. Также здесь необходима проверка типизации кода для избежания проблем в будущем.
* Перед git push - пакет для быстрой проверки логики, наличия мертвого кода, приведения кода к стандарту компании и
улучшения читабельности, наличия документаций.
* Передиоческая проверка - пакет для быстрого поиска возможных логических ошибок, проверки сложности кода, наличия
документаций, правильности указания импортов. А также линтер для сбора метрик.

## Наполнение пакетов
### Пакет проверки при коммите
Так как ещё на этапе коммита нужно выявить все возможные логические ошибки предлагается использовать **pylint**. Это
очень сильный логический линтер, который способен выявлять баги на ранней стадии. Единственным существенным его 
недостатком является долгая проверка, что не позволяет эффективно использовать его для проверки всего проекта.  
Для приведения всего кода под стандарт *pep8* предлагается использовать **autopep8**. С использованием этого
стилистического линтера весь код будет достаточно систематизирован для дальнейшей работы. Это необходимо для
избежания проблем с разными стилями имен, длиной строк и подобным. Далее инструмент окажется мало полезен.  
На этапе коммита также необходимо проверить типы данных. Для этого использует линтер проверки типизации **mypy**.
Чем раньше будут выявлены проблемы с типизацией, тем легче их будет решить.

### Пакет проверки при пуше
При увеличении проверки программного кода время проверки таких грузных линтеров как **pylint** значительно
увеличивается. Предлагается использовать логический линтер **ruff**. Он находит меньше ошибок, но работает
значительно быстрее и обеспечивает достаточный уровень проверки.  
На этапе пуша не должно оставаться не нужного кода. С его обнаружением справится **vulture**. Это линтер для 
обнаружения ненужного и не используещегося кода. Он также показывыает вероятность правильности своего предположения.  
**pydocstyle** проверяет наличие наличие doc string для методов и функций. Это позволит сделать как можно более
подробную документацию и упростить работу в команде.  
Для хорошей проверки кода, где ревьюер не отвлекается на нужные детали хорошо было бы привести код единому стилю.
С этим справляется линтер **black**, который просто настроить на нужды проекта, и который сам форматирует под эти
нужды код так, что он становится легко читаемым.

### Пакет для периодической проверки
Так как над кодом постоянно ведется работа, вносятся правки и идет сопровождение проекта, то необходимо обеспечить 
защиту от возможных логических ошибок, которые вне всей системы не видно. Из-за объемов проектов предлагается
использовать **ruff**. Это позволит быстро проверять код и составлять список необходимых изменений. Удобство
заключается не только в скорости проверки, но и возможности форматирования некоторого количества ошибок сразу после
проверки. Также существует возможность с помощью **ruff** вывести все возникшие ошибки в отдельный файл и составить
баг репорт.  
Для того, чтобы в сопровождении не было проблем с выяснением зачем и для чего были написаны те или иные
фрагменты кода следует проверить есть ли doc string везде где он возможен с помощью **pydocstyle**.  
По той же причине следует правильно расположить импорты проекта с помощью линтера форматирования **isort**.
Чтобы понимание проекта было полным необходимо получать данные метрик и code complexity с помощью **Radon**.