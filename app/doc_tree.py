class DocTree():
    def __init__(self, url):
        self.url = url
        self._branches = []

    def get_branches(self):
        return self._branches

    def set_branches(self, value):
        self._branches = value
        print("[Set]: Doc tree branches update.")

    def del_branches(self):
        self._branches = []
        print("Doc tree branches cleared.")

    branches = property(get_branches, set_branches, del_branches, "I am branches.")
