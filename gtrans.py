import re
import urllib

import simplejson as json


class UrlOpener(urllib.FancyURLopener):
	version = "py-gtranslate/1.0"

class InvalidLanguage(Exception): pass
class UnableToDetectLanguage(Exception): pass

base_uri = "http://ajax.googleapis.com/ajax/services/language/translate"
detect_uri = "http://ajax.googleapis.com/ajax/services/language/detect"
default_params = {'v': '1.0'}
langs = json.load(file('langs.json', 'r'))

def _build_args(dict):
	args = default_params.copy()
	args.update(dict)
	return '&'.join(['%s=%s' % (k,v) for (k,v) in args.iteritems()])

def detect_lang(phrase):
	args = {'q': urllib.quote_plus(phrase)}
	resp = json.load(UrlOpener().open('%s?%s' % (detect_uri, _build_args(args))))
	try:
		return resp['responseData']['language']
	except:
		raise UnableToDetectLanguage()

def translate(phrase, to, src="auto"):
	if src == "auto":
		src = detect_lang(phrase)
	src = langs.get(src, src)
	to = langs.get(to, to)
	if not src in langs.values() or not to in langs.values():
		raise InvalidLanguage("%s=>%s is not a valid translation" % (src, to))
	
	args = {
		'langpair': '%s%%7C%s' % (src, to),
		'q': urllib.quote_plus(phrase),
	}
	resp = json.load(UrlOpener().open('%s?%s' % (base_uri, _build_args(args))))
	try:
		return resp['responseData']['translatedText']
	except:
		# should probably warn about failed translation
		return phrase
