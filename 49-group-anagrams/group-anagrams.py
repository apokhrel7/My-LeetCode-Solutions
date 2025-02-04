class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each character of each word,

        # use hashmap to count occurances of letters in order to group the letters

    

        dict = {}
        res = []

        

        for word in strs:
            dict[''.join(sorted(word))] = []

        for word in strs:
            dict[''.join(sorted(word))].append(word)

        for word in dict.values():
            res.append(word)

        return res


        


        