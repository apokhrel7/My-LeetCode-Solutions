class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. sort each word and add it to a hash map. this way we can group anagrams later
        2. go through list of strings, sort the string, add it to the corresponding list according to the sorted words hashset
        """

        hash_map = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            hash_map[sorted_word] = []

        # {ate: [], bat: [], ant: []}
        res = []

        for word in strs:
            sorted_word = ''.join(sorted(word))
            hash_map[sorted_word].append(word)

        for list_words in hash_map.values():
            res.append(list_words)

        return res


        
