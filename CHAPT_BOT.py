import wolframalpha
import wikipedia
import pyttsx3
#  AUDIO ENGINE...............................

# Audio output to user by Assistent...........
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#  USING WOLFRAME_API_KEY...................
appId = '97U4GL-TYHG9YU349'
client = wolframalpha.Client(appId)
# method that search wikipedia...
def search_wiki(keyword=''):
    # running the query
    searchResults = wikipedia.search(keyword)
    # If there is no result, print no result
    if not searchResults:
        print("No result from Wikipedia")
        return
    # Search for page... try block
    try:
        page = wikipedia.page(searchResults[0])
    except wikipedia.DisambiguationError as err:
        page = wikipedia.page(err.options[0])

    wikiTitle = str(page.title.encode('utf-8'))
    wikiSummary = str(page.summary.encode('utf-8'))
    print(wikiSummary)


def search(text=''):
    res = client.query(text)
    # Wolfram cannot resolve the question
    if res['@success'] == 'false':
        print('Question cannot be resolved')
    # Wolfram was able to resolve question
    else:
        result = ''
        # pod[0] is the question
        pod0 = res['pod'][0]
        # pod[1] may contains the answer
        pod1 = res['pod'][1]
        # checking if pod1 has primary=true or title=result|definition
        if (('definition' in pod1['@title'].lower()) or ('result' in pod1['@title'].lower()) or (
                pod1.get('@primary', 'false') == 'true')):
            # extracting result from pod1
            result = resolveListOrDict(pod1['subpod'])
            print(result)
            return result
            question = resolveListOrDict(pod0['subpod'])
            question = removeBrackets(question)
            # primaryImage(question)
        else:
            # extracting wolfram question interpretation from pod0
            question = resolveListOrDict(pod0['subpod'])
            # removing unnecessary parenthesis
            question = removeBrackets(question)
            # searching for response from wikipedia
            search_wiki(question)
            # primaryImage(question)
def removeBrackets(variable):
    return variable.split('(')[0]
def resolveListOrDict(variable):
    if isinstance(variable, list):
        return variable[0]['plaintext']
    else:
        return variable['plaintext']

while True:
    print('\nHi,how can i help you\n')
    q = input("type something...\t")
    aud_output = search(q)
    speak(aud_output)





