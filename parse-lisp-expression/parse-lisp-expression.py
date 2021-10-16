// https://leetcode.com/problems/parse-lisp-expression

class Solution(object):
    def evaluate(self, expr):
        """
        :type expression: str
        :rtype: int
        """
        def tokenizer(expr):
            return expr.replace('(', '( ').replace(')', ' )').split()

        def eva(tokens, env):
            if tokens[0] != '(':
                if tokens[0][0] in '-1234567890':
                    return int(tokens.popleft())
                else:
                    return env[tokens.popleft()]
            else:
                # (let|add|mul ...)))))
                tokens.popleft()
                if tokens[0] in ('add', 'mult'):
                    op = tokens.popleft()
                    a, b = eva(tokens, env), eva(tokens, env)
                    val = a + b if op == 'add' else a * b
                else: # let
                    tokens.popleft()
                    local = env.copy()
                    while tokens[0] != '(' and tokens[1] != ')': # here we peek the second token
                        var = tokens.popleft()
                        local[var] = eva(tokens, local)
                    val = eva(tokens, local)

                # skip the matching )
                tokens.popleft()
                return val

        tokens = collections.deque(tokenizer(expr))
        env = {}

        return eva(tokens, env)