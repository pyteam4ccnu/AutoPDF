class DocTree():
    """
    This class is node of Doc Tree.
    """
    def __init__(self, url):
        """
        Init function.
        :param url: This node's url.
        """
        self.url = url
        self._branches = []

    def get_branches(self):
        """
        This function is branches property's getter.
        :return: This node's branches.
        """
        return self._branches

    def set_branches(self, value):
        """
        This function is branched property's setter.
        :param value: new branches(old_branches.append(new_children))
        :return:
        """
        self._branches = value
        print("[Set]: Doc tree branches update.")

    def del_branches(self):
        """
        This function is branches property's del.
        :return:
        """
        self._branches = []
        print("Doc tree branches cleared.")

    branches = property(get_branches, set_branches, del_branches, "I am branches.")
