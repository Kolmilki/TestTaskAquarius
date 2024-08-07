# Сравнение стилистических линтеров для **Python**
На втором этапе сравним линтеры, основная задача которых форматирование. Существует множество разных стайлинговых линтеров.
Например есть pydocstyle, который проверяет только docstring, или, например, pycodestyle, который замечает в коде только
отклоненния от pep8. Есть также те, которые занимаются автоматическим форматированием. Например black или Isort.

В сравнении участвует несколько линтеров для форматирования и стилизации кода:
* **black** - форматирующий линтер для автоматического исправления кода под стандарты разработки и удобного чтения.
* **autopep8** - ещё один форматирующий линтер для стандартизации кода под pep8.
* **flake8** - пакет линтеров для проверки логики кода, его стиля и сложности с последующим выводом ошибок в
предпочтительный формат.
* **isort** - линтер, который может правильно рассортировать ваши импорты, опираясь на стандарты их расположения.

---
## Удобство использования
В основном этот параметр определяется тем, насколько удобно внедрять линтер в тот или иной проект. Если линтер 
приходится перенастраивать несколько недель, так как стандарты линтера совсем не подходят под требования, значит линтер
либо неудобен в использовании, либо вовсе не нужен в проекте.
### **black**
Black поддерживает версии python начиная с 3.3 вплоть до 3.13 и для того чтобы black опирался на стандарты именно нужной
версии необходимо лишь поменять целевую версию с помощью тега ```-t[python_version]```. Есть возможность настроить 
форматирование только для определенных сценариев, а в остальных случаях игнорировать ошибки стиля. Также есть
возможность превью изменения перед автоматическим форматированием. Есть возможность ускорения работы, однако, это
выключает проверку безопасности кода *AST safety test*.  
Для расширенной настройки black можно считать подготовленный конфигурационный файл с помощью команды
```--config FILE```.
```commandline
usage: black [OPTIONS] SRC ...
```
### **autopep8**
Как и следует из названия линтер форматирует код под современный стандарт *pep8*. Из возможностей настройки доступны
следующие опции:
* ```-d, --diff``` *- показывает изменения в отформатированном файле*
* ```--ignore-local-config``` *- форматирует выбранные файлы под требования указанные в конфигурационном файле*
* ```-a --agressive``` *- игнорирование множественных пробелов, а также отсутствия пробелов*
*  ```ignore/select errors``` *- игнорирование определенных ошибок или обращение внимания только на определенные ошибки*
*  ```--exit-code``` *- изменяет код с которым завершается форматирование*
```commandline
usage: autopep8 [files ...]
```

### **flake8**
Этот пакет линтеров позволяет настраивать как отдельные свои модули, так и всю связку целиком. Есть возможность
настроить вывод в отдельный файл. Также сущетсвует возможность запуска flake8 вместе с дополнительными конфигурационными
файлами, что позволяет легко встроить требования компании в проверку или игнорировать все конфигурационные файлы если
необходимость в требованиях пропадет.  
Из уникальных команд можно выделить команду ```--benchmark```, которая запускает бенчмарк для наблюдения за состоянием
проверки, а также команду ```--bug-report```, которая составляет json файл с информацией для баг репорта.  
Из не уникальных команд тут есть те, что позволяют игнорировать ошибки, форматировать код включением модулей
автоматического форматирования, игнорировать определенные файлы и изменять код завершения работы линтера.  
Также у flake8 доступен предустановленный плагин pep8_naming. Опций предоставляется немного. Всего три:
* ```--ignore-names``` *- для игнорирования определенных имен*
* ```--classmethod-decorators``` *- для указания имен декораторов, которые линтер должен считать классами*
* ```--staticmethod-decorators``` *- для указания имен декораторов, которые линтер должен считать статическими методами*
```commandline
usage: flake8 [options] file file ...
```

### **isort**
Линтер, который, казалось бы, предлагает совсем небольшой функционал, обладает огромным количеством настроек. 
Предлагается 252 возможных опции, которыми можно настроить импорт под какой угодно стандарт. Среди этих настроек есть
определение конкретных мест для импортов, определение будущих импортов, переименование импортов под стандарты,
уменьшение длинны строки импорта, перемещение всех импортов в одну строчку и, конечно, сортировка импортов под 
установленные стандарты. А также множество других опций.
```commandline
usage: isort [files ...]
```
---
## Влияние на код
Этот параметр определяет насколько важны изменения, которые будут предложены или внесены тем или иным линтером. Возможно
в трате времени на настройку конфигурации и проходку по всем модулям нет смысла, так как изменения в коде будут 
совершенно незначительны.
### **black**
Как линтер, основные задачи которого приведение кода к стандарту и улучшение читабельности, справляется он отлично. Все
строки кода, которые были заполнены плохо читающейся информацией были разбиты на более мелкие, из которых информация
считывается быстро. Также были устранены несооветствия стандарту pep8.
### **autopep8**
После отработки линтера black autopep8 оставляет смешанные впечатления. При запуске автоформатирования он перестраивает
код под стандарты pep8, но выглядит это неприятно и ухудшает читабельность. Так что после предыдущего линтера смысла в 
запуске второго не много. Только если команда строго следует всем правилам в документации основного стиля Python. В 
целом линтер действует по принципу "необходимое и достаточное".   
Запуск линтера проходил со следующими атрибутами:
```autopep8 --in-place --aggressive```
### **flake8**
Кроме логической составляющей flake8, которая способна обнаруживать неиспользованные импорты, существует также
стилистическая, которая может увидеть слишком длинные строки, что не нужно после использования black, так как при 
правильной настройке всё уже будет выравнено по стандарту разработки. Также у flake8 присутствует встроенный плагин,
который проверяет несоответствие имен с выбранной методологией.
### **isort**
Полезный инструмент для приведения блока импортов к стандарту pep8, но не слишком нужный для постоянного использования.
Так что верным решением будет использование этого линтера в конце рабочего этапа. Когда будет понятно, что если импорт
не использовался, то он и не нужен, а если использовался, то он должен быть на назначенном ему месте.

---
## Полезность
Данный критерий скорее опреляет необходимую частоту использований, нежели является параметров выбора линтера.
Все рассматриваемые линтеры по своему полезны, но необходимости использовать каждый из них каждый раз как происходит
коммит нет. Поэтому определим - какие линтеры важно запускать на каждый этап, а какие нужны не так часто.
### 1. Этап git commit
   * #### **flake8**
        Перед коммитом необходимо проверить базовые ошибки. Такие как несоответствие имен, слишком длинные строки, 
логические ошибки, которые могут привести к проблемам в дальнейшем.
   * #### **autopep8**
        Далее следует привести код к единообразию стиля. Хоть код может казаться программисту очень хорошим и
соответствующим всем стандартам - это может быть не так. Необходима тщательная проверка на соответствие стандарту.
### 2. Этап git push
   * #### **black**
        Перед отправление кода в удаленный репозиторий важно сделать его хорошо читаемым для упрощения pull request или
merge request.
### 3. Этап проверки всего проекта
   * #### **isort**
        На этапе проверки кода проекта все мелкие допущения должны быть устранены. При дальнейшем сопровождении
написанного проекта код должен легко читаться, а все его структуры должны быть расположены на своих местах. В том
порядке, который используется разработчиками как стандарт. Импорты также являются частью этого условия. И хоть при
активной, частой работе с кодом порядок импортов не имеет значения, он должен стандартизирован хотя бы конце каждого
этапа разработки. 

---
# **Итоги**
Стилистические линтеры очень разные по назначению, но очень схожие по смыслу. Все они предназначены для стандартизации
кода и упрощения его читабельности и при этом каждый решает разные задачи. Даже похожие по принципу стандартизации
линтеры, такие как *black* и *autopep8*, по сути, приводят код к нужному результату разными путями. *Autopep8* не
преследует других целей, кроме как приведение кода к pep8. В этом смысле *black* выигрывает, не только подводя код к
стандарту, но и улучшая читабельность.  
Считаю, что наиболее полезные стилистические линтеры это *flake8*, как удобный инструмент для предварительной проверки
не только стиля, но и логики кода, и *black*, как отличный инструмент повышения читабельности. *isort* тоже хороший
линтер для стандартизации кода, однако, необходимый только для поздних этапов проверки. autopep8 слишком ситуативный и
во многом проигрывает линтерам, которые выполняют не только одну задачу. Он полезен, но далеко не всегда. Можно его
использовать, но каких-то особых улучшений он не дает.
