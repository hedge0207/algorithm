import os


class Updater:
    MARKDOWN_FORMAT = ".md"

    def __init__(self):
        self.text = ""
    
    def make_text(self, d, cur_dir):
        for path in os.listdir(cur_dir):
            if path == ".git" or path == ".idea":
                continue

            new_path = "{}/{}".format(cur_dir, path)
            print(new_path)
            if new_path == "./.gitignore":
                continue

            if os.path.isdir(new_path):
                if new_path.count(".") > 1:
                    continue
                self.text += "{} {}\n".format("#"*d, path)
                self.make_text(d+1, new_path)
            else:
                self.text += "{}\n".format(os.path.splitext(new_path)[0].split("/")[-1])
            self.text += "\n"
                
    def update(self):
        with open("./README.md", "w", encoding="utf8") as f:
            self.make_text(1, ".")
            f.write(self.text)

    

if __name__ == "__main__":
    updater = Updater()
    updater.update()