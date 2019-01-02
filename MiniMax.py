from random import randint
class node:
    def __init__(self, child, layer):
        self.val = randint(-50, 50)
        self.child = child
        self.children = [None, None]
        self.layer = layer
        
        if child:
            self.children[0] = node(layer < 2, self.layer + 1)
            self.children[1] = node(layer < 2, self.layer + 1)
#        if child:
#            for i in range(0, 2):
#                if randint(0, 1) == 1:
#                    self.children[i] = node(False)
#                else:
#                    self.children[i] = node(True)

    def show(self):
        #print(self.val, self.layer)
        l = [0, 0]

        if self.child:
            l[0] = self.children[0].val
            l[1] = self.children[1].val
            print(l)

            self.children[0].show()
            self.children[1].show()



node = node(True, 1)
print(node.val)
node.show()
        
