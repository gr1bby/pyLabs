class Storage:

    def __init__(self):
        self.storage = list()
        self.is_appendable = False


    def show(self):
        print(self.storage)


    def append(self, *args):
        if self.is_appendable:
            for arg in args:
                self.storage.append(arg)
        else:
            print("You should to unlock storage.")


    def lock(self):
        self.is_appendable = False


    def unlock(self):
        self.is_appendable = True


    def __enter__(self):
        if not self.is_appendable:
            self.is_appendable = True
        return self

    
    def __exit__(self, *exc_details):
        self.is_appendable = False


if __name__ == '__main__':
    with Storage() as st:
        st.append(1, '2', [3, '4'])
        st.show()
        st.lock()
        st.append([1, 2, 3])
        st.unlock()
        st.append([1, 2, 3])
        st.show()
