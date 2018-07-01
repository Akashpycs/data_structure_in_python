"""multiple inheritance class"""
from linkedbinarytree import LinkedBinaryTree
from map_base import MapBase

class TreeMap(LinkedBinaryTree, MapBase):
    #------overide Position class-------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key
            
        def value(self):
            return self.element()._value
    #------Nonpublic utilities---------------
    def _subtree_search(self, p, k):
        """return Position of p's subtree key k or last node searched"""
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        #unsuccesful search and return the last position searched
        return p
    
    def _subtree_first_position(self, p):
        """return Position of first item in subtree rooted at p"""
        """will be used by before()"""
        walk = p
        #recursivly walking to the left child until the left subtree has no child
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk
    
    def _subtree_last_position(self, p):
        """return Position of last item in subtree rooted at p"""
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk
    #--------public accessors ----------------
    def first(self):
        return self._subtree_first_position(self.root()) if len(self)>0 else None
    
    def last(self):
        return self._subtree_last_position(self.root()) if len(self)>0 else None
    
    def before(self, p):
        """returns the position that is immediately before position p
        in natural order of the keys"""
        self._validate(p)
        # if there is a left subtree, then the first positiion of in subtree 
        # rooted at the left(p) will be the immediate position before p
        if self.left(p) is not None:
            return self._subtree_first_position(self.left(p))
        # if there is no left substree, 
        # the immediate smaller position will be the parent of the "left turn" position
        # when going upward. 
        else: 
            walk = p
            above = self.parent(walk)
            # not None is the boundary for root node
            # walk == self.left(above) is the marker for "left turn"
            while above is not None and walk==self.left(above):
                walk = above
                above = self.parent(walk)
            return above
    
    def after(self, p):
        """returns the position that is immediately after position p
        in natural order of the keys"""
        self._validate(p)
        # if there exists p's right child, successor is left most position
        # in p's right subtree
        if self.right(p) is not None:
            walk = self.right(p)
            while self.left(walk)is not None:
                walk = left(walk)
            return walk
        # successor is the parent of the "right turn" position 
        # when going upward
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk==self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            #self._rebalance_access(p) 
            return p
    
    def find_min(self):
        """return(key, value) pair with minumum key; it's different
        from first() which only return the position with the minumum key
        """
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())
    
    def __getitem__(self, k):
        """return value associated with key k; raise KeyError if not found"""
        if self.is_empty():
            raise KeyError('key Error:' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            #self._rebalance_access(p)
            #this might be an unsuccessful search, so deal with this...
            if k!=p.key():
                raise KeyError('key error:'+repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """assign v to k, overwrite v if k present"""
        #if tree is empty
        if self.is_empty():
            leaf = self._add_root(self._Item(k,v)) # inherited from LinkedBinaryTree class
        else:
            p = self._subtree_search(self.root(), k)
            #if k is present in current tree
            if p.key() == k:
                #it's not p.value()!!
                p.element()._value = v
                #self._rebalance_access(p)
                return
            #didn't find k in current tree; create a new object of Item
            # and add to either left or right of the last node searched
            else:
                item = self._Item(k, v)
                if k > p.key():
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
            #self._rebalance_insert(leaf)

    def __iter__(self):
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)
    
    def delete(self, p):
        self._validate(p)
        if self.left(p) and self.right(p):
            # replacement is the node with the greatest k in left substree
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element()) # _replace is from LinkedBinaryTree class
            p = replacement # replace position reference
        # parent = self.parent(p)
        # node p now only has one child at most
        self._delete(p) # refer to LinkedBinaryTree class
        # self._rebalance_delete(parent)

    def __delitem__(self, k):
        """remove item associated with k """
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            #self._rebalance_access(p)
        raise KeyError('Key Error:' + repr(k))


    def find_ge(self, k):
        """return key, value pairs with least key greater or equal to 
        k; return None is there doesn't exist such a key"""
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            if p is not None:
                return (p.key(), p.value())
            else: 
                return None










