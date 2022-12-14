class datei:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size


class folder:
    def __init__(self, parent, name):
        self.name = name
        if self.name == '/':
            self.parent = None
        else:
            self.parent = parent
        self.subfolder = []
        self.files = []

    def __repr__(self):
        return f"{self.name}"

    def make_subfolder(self, name):
        new_folder = folder(self, name)
        self.subfolder.append(new_folder)

    def add_content(self, datei_neu: datei):
        duplicate = False
        for datei in self.files:
            if datei_neu.get_name() == datei.get_name():
                duplicate = True

        if not duplicate:
            self.files.append(datei_neu)

    def get_size(self):
        out = 0
        if not len(self.files) == 0:
            for foo in self.files:
                out += foo.get_size()
        if not len(self.subfolder) == 0:
            for bar in self.subfolder:
                out += bar.get_size()
        return out

    def get_name(self):
        return self.name

    def go_up(self):
        if self.name == '/':
            return self
        else:
            return self.parent

    def go_down(self, name):
        for foo in self.subfolder:
            if foo.name == name:
                return foo

    def get_subfolders(self):
        return self.subfolder

    def has_subfolders(self):
        return len(self.subfolder) > 0


class navigator:
    def __init__(self):
        self.current_folder = folder('bob', '/')
        self.tld = self.current_folder

    def get_current_folder(self):
        return self.current_folder

    def get_tld(self):
        return self.tld

    def run_line(self,line_input):
        if line_input[0] == "$":
            line_input = line_input.strip('$ ')
            if line_input == "cd ..":
                self.current_folder = self.current_folder.go_up()
            elif "cd" in line_input:
                goto = line_input.strip('cd ')
                self.current_folder = self.current_folder.go_down(goto)
            #elif "ls" in line_input:
             ##   continue
        else:
            if "dir" in line_input:
                self.current_folder.make_subfolder(line_input.strip('dir ').replace('\n',''))
            else:
                file_infos = line_input.split()
                new_one = datei(file_infos[1].replace('\n',''), int(file_infos[0]))
                self.current_folder.add_content(new_one)

    def get_folders(self, foldernow):
        all_folders = [foldernow]
        if foldernow.has_subfolders():
            for fold in foldernow.get_subfolders():
                all_folders.append(fold)
        return all_folders

navi = navigator()
print(navi.get_current_folder().get_name())
with open("input","r") as file:
    for line in file:
        if not "/" in line:
            print(line)
            navi.run_line(line)
            print(navi.get_current_folder())
print(navi.get_folders())
