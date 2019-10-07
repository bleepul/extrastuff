from cmd import Cmd

from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
d = GraphDatabase.driver(uri, auth=("neo4j", "UseCases"))
txn = d.session()


class MyPrompt(Cmd):
    prompt = 'UseCases> '
    intro = "Welcome! Type ? to list commands"

    def do_exit(self, inp):
        print("Bye")
        return True

    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')

    def do_add_node(self, inp):
        print("adding '{}'".format(inp))

    def help_add(self):
        print("Add a new entry to the system.")

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)

        print("Default: {}".format(inp))

    do_EOF = do_exit
    help_EOF = help_exit


if __name__ == '__main__':
    MyPrompt().cmdloop()