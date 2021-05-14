class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        
        def splitter(fragment):
            f_len = len(fragment)
            for index in range(1, f_len+1):
                left, right = fragment[:index], fragment[index:]
                if (
                    (not left.startswith('0') or left == '0')
                    and
                    (not right.endswith('0'))
                    ):
                    yield left + ('.' if index != f_len else '') + right

        s = s[1:-1] # remove ( and )
        
        return [
            f"({long_lat[0]}, {long_lat[1]})"
            for i in range(1, len(s))
            for long_lat in itertools.product(splitter(s[:i]), splitter(s[i:]))
            ]