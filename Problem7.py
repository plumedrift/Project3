# The Router class will wrap the Trie and handle
class Router:
    def __init__(self):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = RouteTrie()

    def add_handler(self, path, handler):
        # Add a handler for a path
        self.routeTrie.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        return self.routeTrie.find(path)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode("Home Page Handler")

    def insert(self, path, handler=None):
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        words = path.split('/')

        if not handler:
            handler = " ".join(words[1:])
            handler += " handler"

        for i in range(len(words)):
            if words[i] and words[i] not in current_node.children:
                if i == len(words) - 1:
                    current_node.children[words[i]] = RouteTrieNode(handler)
                else:
                    current_node.children[words[i]] = RouteTrieNode()
                    current_node = current_node.children[words[i]]
            elif words[i]:
                current_node = current_node.children[words[i]]

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        words = path.split('/')
        handler = 'not found handler'

        if not path or path == '/':
            handler = self.root.handler

        for word in words:
            if word and word in current_node.children:
                current_node = current_node.children[word]
                if current_node.handler:
                    handler = current_node.handler
                else:
                    handler = 'not found handler'
            elif word:
                handler = 'not found handler'

        return handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler


# create the router and add a route
router = Router()
router.add_handler("/home/about", "about handler")  # add a route

print("[Edge Case]")
print(router.lookup("/"))
print()
# 'Home Page Handler'

print("[Edge Case]")
print(router.lookup(""))
print()
# 'Home Page handler'

print(router.lookup("/home"))
print()
# 'not found handler'

print(router.lookup("/home/about"))
print()
# 'about handler'

print(router.lookup("/home/about/"))
print()
# 'about handler'

print(router.lookup("/home/about/me"))
print()
# 'not found handler
