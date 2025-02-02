class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        if not strs:
            return ""
        for str in strs:
            result += str+'-enCodeStr-'
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        if s == "":  # Special case for empty list
            return []
        result_array = s.split('-enCodeStr-')
        print("result array \n", result_array)
        new_result_array = result_array[:-1]
        return new_result_array
