import own_db_tree
import sec_tree
import third_tree
import ascii_value

def printing(node):
    if node is not None:
        printing(node.left)
        if node.sec_data is not None:
            print(node.sec_data)
        printing(node.right)

first_tree = own_db_tree.tree
sec__tree = sec_tree.tree
def connection_test(ftree, name):
    if ftree is not None:
        connection_test(ftree.left, name)
        if ftree.data == name[0]:
            sec_tree_con_test(sec__tree, len(name), name)
            return

        connection_test(ftree.right, name)


def sec_tree_con_test(sec__tre, length, name):
    if sec__tre is not None:
        sec_tree_con_test(sec__tre.left, length, name)
        if sec__tre.data == length:
            sec__tre.sec_data = name
            print("We found for third tree")

            for char in name:
                se_value = ord(char)

                third_tre = third_tree.ThirdNode(char, se_value)
                third_trees = third_tree.third_insertion(sec__tree.sec_data, se_value, third_tre)
                print("print third tree", char, se_value)
            sec_tree_con_test(sec__tre.right, length, name)
            return
        sec_tree_con_test(sec__tre.right, length, name)

if __name__ == '__main__':
    while True:
        ascii_value.link()
        connection_test(first_tree, ascii_value.link())
        printing(sec__tree)
        third_tree.third_insertion()
