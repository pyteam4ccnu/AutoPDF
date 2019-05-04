class DocTree():
    url = ""
    _branches = []

    def __init__(self, url):
        self.url = url

    def get_branches(self):
        return self._branches

    def set_branches(self, branches):
        self._branches = branches
        print("Doc tree branches update.")

    def del_branches(self):
        self._branches = []
        print("Doc tree branches cleared.")

    branches = property(get_branches, set_branches, del_branches, "I am branches.")
