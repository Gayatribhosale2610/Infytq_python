'''write a python function translate() that accepts the bilingual dictionary and a list of English words (your Christmas wish) and returns a list of equivalent Swedish words. '''

def translate(bilingual_dict,english_words_list):
    swedish_words_list = []
    for i in english_words_list:
        if i in bilingual_dict:
            swedish_words_list.append(bilingual_dict[i])
    return swedish_words_list
  
bilingual_dict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english_words_list=["merry","christmas", "and"]
print("The bilingual dict is:",bilingual_dict)
print("The english words are:",english_words_list)
swedish_words_list=translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:",swedish_words_list)
