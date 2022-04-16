class MyQueue:
    
    def __init__(self):
        self.stack = []
        self.tmp_stack = []

    def push(self, x: int) -> None:
        while self.stack:
            self.tmp_stack.append(self.stack.pop())
        self.stack.append(x)
        
        while self.tmp_stack:
            self.stack.append(self.tmp_stack.pop())

    def pop(self) -> int:
        return self.stack.pop()
    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack
    
################## Soln1 #############
#     def __init__(self):
#         self.stack = []
#         self.tmp_stack = []

#     def push(self, x: int) -> None:
#         self.stack.append(x)

#     def pop(self) -> int:
#         if self.stack:
#             while len(self.stack)!=1:
#                 self.tmp_stack.append(self.stack.pop(-1))
#             ans = self.stack.pop(-1)
#             while self.tmp_stack:
#                 self.stack.append(self.tmp_stack.pop(-1))
#             return ans
#         else:
#             return None

#     def peek(self) -> int:
#         if self.stack:
#             while len(self.stack)!=1:
#                 self.tmp_stack.append(self.stack.pop(-1))
#             ans = self.stack[-1]
#             while self.tmp_stack:
#                 self.stack.append(self.tmp_stack.pop(-1))
#             return ans
#         else:
#             return None


#     def empty(self) -> bool:
#         return self.stack == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()