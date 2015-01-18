# periscope
Subtitles adapter.

Установка
===============
    pip install -r requirements.txt

Из консоли:
    
    import nltk
    nltk.download('all')
    nltk.download('punkt')

Запуск
===============
1.Создаем словарь.В репозитории уже есть книга,чарли и шоколадная фабрика,но вы должны использовать свою.
    
    python booksparser.py charlieandchocolatefactory.txt

2.Запускаем парсер.

    python parse.py file "path/to/file can be even with spaces"
    python parse.py directory "path/to/directory also can contain spaces"

В том случае если что-то пойдет не так,файл с субтитрами вы не потеряете.К нему можно будет обратиться с приставкой OLD.Пример:
    
    python parse.py file ~/Downloads/Whi pla sh.srt
    Что-то пошло не так...
    
    python parse.py file ~/Downloads/Whi pla shOLD.srt
        
    
