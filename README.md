# py-gtranslate

A Library for using Google Translate in Python


## Usage

        >>> import gtrans
        >>> gtrans.translate(src="english", to="spanish", phrase="Hello World")
        u'Hola Mundo'
        >>> gtrans.translate(src="spanish", to="english", phrase="Hola Mundo")
        u'Hello World'
