import requests
import openai

# keys
openaikey = ""


# Saves sightwords to a list
def load_sight_words():
    f = open('sightwords.txt', 'r')
    sight_words = f.read()
    sight_words_list = sight_words.split()
    f.close()
    return sight_words_list


# Save the graphemes to a list
def load_graphemes():
    f = open('graphemes.txt', 'r')
    graphemes = f.read()
    graphemes_list = graphemes.split()
    f.close()
    return graphemes_list


def get_target_grapheme(grapheme_list):
    student_level = int(input("What level is the student at?"))
    target_grapheme = grapheme_list[student_level]
    return target_grapheme


# Need to cull the list of generated words to remove words with
def get_grapheme_words(target_grapheme):
    url = "http://api.datamuse.com/words?sp=*" + target_grapheme + "*"
    response = requests.get(url)
    words = response.json()
    return [word["word"] for word in words]

def sort_grapheme_words_by_length(grapheme_words):
    return sorted(grapheme_words, key=len)


def main():
    sight_words_list = load_sight_words()
    grapheme_list = load_graphemes()
    target_grapheme = get_target_grapheme(grapheme_list)
    grapheme_words = get_grapheme_words(target_grapheme)
    grapheme_words = sort_grapheme_words_by_length(grapheme_words)
    print(grapheme_words)


if __name__ == '__main__':
    main()
