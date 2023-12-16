class SimpleUnixSystemWithCat:
    def __init__(self):
        self.current_directory = "/"
        self.file_system = {"/": {}}

    def run(self):
        while True:
            command = input(f"{self.current_directory}$ ").strip().split()
            if not command:
                continue

            if command[0] == "exit":
                break
            elif command[0] == "ls":
                self.ls("-la" in command)
            elif command[0] == "cd" and len(command) > 1:
                self.cd(command[1])
            elif command[0] == "mkdir" and len(command) > 1:
                self.mkdir(command[1])
            elif command[0] == "touch" and len(command) > 1:
                self.touch(command[1])
            elif command[0] == "echo" and ">" in command:
                self.echo(command)
            elif command[0] == "cat" and len(command) > 1:
                self.cat(command[1])
            else:
                print("Invalid command or missing argument.")

    def ls(self, show_all=False):
        directories = [key for key in self.file_system if key.startswith(self.current_directory) and key != self.current_directory]
        files_and_dirs = set()

        for dir in directories:
            sub_path = dir[len(self.current_directory):].strip("/").split("/", 1)
            if len(sub_path) == 1:
                item = sub_path[0] + "/"
                if not item.startswith(".") or show_all:
                    files_and_dirs.add(item)
            else:
                item = sub_path[0] + "/"
                if not item.startswith(".") or show_all:
                    files_and_dirs.add(item)

        # Add files in the current directory
        for item in self.file_system.get(self.current_directory, {}).keys():
            if not item.startswith(".") or show_all:
                files_and_dirs.add(item)

        for item in sorted(files_and_dirs):
            print(item)

    def cd(self, path):
        if path == "..":
            if self.current_directory != "/":
                self.current_directory = "/".join(self.current_directory.rstrip("/").split("/")[:-1])
                if not self.current_directory:
                    self.current_directory = "/"
        elif path.startswith("/"):
            if path in self.file_system:
                self.current_directory = path
            else:
                print("Directory not found.")
        else:
            new_path = f"{self.current_directory.rstrip('/')}/{path}"
            if new_path in self.file_system:
                self.current_directory = new_path
            else:
                print("Directory not found.")

    def mkdir(self, directory_name):
        new_path = f"{self.current_directory.rstrip('/')}/{directory_name}"
        if new_path not in self.file_system:
            self.file_system[new_path] = {}
        else:
            print("Directory already exists.")

    def touch(self, file_name):
        directory = self.file_system.get(self.current_directory, None)
        if directory is not None and file_name not in directory:
            directory[file_name] = ""
        else:
            print("File already exists or invalid directory.")

    def echo(self, command):
        try:
            text_index = command.index(">")
            text = " ".join(command[1:text_index])
            file_name = command[text_index + 1]

            if file_name in self.file_system.get(self.current_directory, {}):
                self.file_system[self.current_directory][file_name] = text
            else:
                print("File does not exist.")
        except (ValueError, IndexError):
            print("Invalid echo command syntax.")

    def cat(self, file_name):
        file_content = self.file_system.get(self.current_directory, {}).get(file_name, None)
        if file_content is not None:
            print(file_content)
        else:
            print("File does not exist.")

# Example usage
system_with_cat = SimpleUnixSystemWithCat()
# Uncomment the line below to run the system. Note that it will enter an interactive mode.
system_with_cat.run()
