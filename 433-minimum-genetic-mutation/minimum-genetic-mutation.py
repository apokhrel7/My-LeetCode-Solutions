from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # This is a graph problem --> BFS
        # We check each letter and change it, if this new word is in the bank, we put it to queue and repeat the process
        # If in the process we have matched to the endGene, return the number of steps it took
        # When we make the new word, take the word from 0...i + new character (any of letter of 'ACGT') + i + 1...
        # If new word is in the bank, just remove the word from the bank instead of keeping a 'visited' set (this prevents us from going through the same potential mutated word again)

        bank = set(bank)

        q = deque([(startGene, 0)])
        characters = ['A', 'C', 'G', 'T']
        

        while q:
            current_sequence, count = q.popleft()

            if current_sequence == endGene: return count

            for i, gene in enumerate(current_sequence):

                # To build new word, replace ith letter with all the possible letters ('A', 'C', 'G', 'T')
                for char in characters:
                    new_word = current_sequence[:i] + char + current_sequence[i + 1:]

                    # if new_word is in the bank, queue that new word and incremement the count
                    # remove the new word from the bank to prevent spanning BFS on the 'visited' word
                    if new_word in bank:
                        q.append((new_word, count + 1))
                        bank.remove(new_word)
                        
        # at this point, we traversed all the combos and no mutations
        return -1



        