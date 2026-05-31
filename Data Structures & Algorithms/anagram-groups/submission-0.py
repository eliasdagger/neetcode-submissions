class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ga = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in ga:
                ga[sorted_word] = []
            
            ga[sorted_word].append(word)




        return list(ga.values())


            

        