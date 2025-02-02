class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = ['!', '?', "'", ',', ';', '.']

        word_dict = {}


        new_paragraph = ''
        for char in paragraph:
            if char in symbols:
                new_paragraph += ' '
            else:  
                new_paragraph += char

        max_count = 0
        max_word = ''
        for char in new_paragraph.split():
            char = char.lower()
            if char not in banned:
                if char not in word_dict:
                    word_dict[char] = 1
                else:
                    word_dict[char] += 1

                if word_dict[char] > max_count:
                    max_count = word_dict[char]
                    max_word = char

        print(word_dict)

        return max_word

        

            

        

         
       

