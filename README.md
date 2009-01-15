# py-gtranslate

A Library for using Google Translate in Python


## Usage

		>>> import gtrans
		>>> gtrans.translate("Hello World!", to="es") # 'src' not specified, language detected
		'Hola Mundo!'
		>>> gtrans.translate("Hola Mundo!", to="french")
		'Bonjour tout le monde!'
		>>> gtrans.translate("Bonjour tout le monde!", to="english", src="fr")
		'Hello everyone!'
