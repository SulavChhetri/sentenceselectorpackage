sentencelist = ['My name is Sulav Thapa.','Mary enjoys cooking.','She likes bananas.','They speak English at work.','The train does not leave at 12 AM.','I have no money at the moment.','Do they talk a lot ?','Does she drink coffee ?','You run to the party.','You have some schoolwork to do.','The train leaves in ten minutes.','Python is a programming langauge.','The name of my country is Nepal.','python dictionary and Json file looks same but are not.','Gabriel Martinelli is my favourite football player.','I am applying for python internship.','This is a list containing sentences.']

dictionary = {}
def datagatherer(list):
    wordlist = []
    for item in list:
        for word in item.split():
            f=filter(str.isalpha,word)
            word="".join(f)
            if word in dictionary.keys():
                dictionary[word].append(item)
            else:
                wordlist.append(item)
                dictionary[word]=wordlist
                wordlist=[]

def searcher(word):
    return dictionary[word]

datagatherer(sentencelist)
if __name__ =='__main__':
    print(searcher('is'))
    print(searcher('python'))
