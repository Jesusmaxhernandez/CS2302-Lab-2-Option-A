# **********************************************************************************************************************
# NAME: Timothy P. McCrary
# CLASS: CS 2302
# LAB 2 OPTION A
# INSTRUCTOR: Diego Aguirre
# TA: Manoj Pravaka Saha
# DATE: 10/17/2018
# PURPOSE: The purpose of this lab was to practice implementing both the Linked List data structure and different
#  sorting algorithms.
# **********************************************************************************************************************


def main():
    id_list = merge_id_files("activision.txt", "vivendi.txt")  # Makes linked list from files.
    id_list_copy = copy_linked_list(id_list)  # Makes copy of first list.
    id_list_copy2 = copy_linked_list(id_list)  # Makes copy of first list.

    # Solution 1 - Finds duplicates iteratively.
    print("__________SOLUTION 1 - NESTED LOOPS CHECK START__________")
    check_id_duplicates(id_list)
    print("__________SOLUTION 1 - END__________")

    # Solution 2 - Sorts list using Bubble Sort then finds duplicates.
    print("__________SOLUTION 2 - BUBBLE SORT CHECK START__________")
    bubble_sort_check(id_list)
    print("__________SOLUTION 2 - END__________")

    # Solution 3 - Sorts list using merge sort then finds duplicates
    print("__________SOLUTION 3 - MERGE SORT CHECK START__________")
    sorted_id_list_copy = merge_sort(id_list_copy)
    count_duplicates(sorted_id_list_copy)
    print("__________SOLUTION 3 - END__________")

    # Solution 4 - Finding duplicates using boolean array.
    print("__________SOLUTION 4 - BOOLEAN ARRAY CHECK START__________")
    boolean_array_check(id_list_copy2)
    print("__________SOLUTION 4 - END__________")


class Node(object):
    item = -1
    next = None

    def __init__(self, item, next):
        self.item = item
        self.next = next

    # Adds a node to the beginning of lined list.
    def add_node(self, item):
        temp = Node(item, self.next)
        self.next = temp

    # Returns size of linked list.
    def size(self):
        current_node = self
        counter = 0
        while current_node is not None:
            counter = counter + 1
            current_node = current_node.next
        return counter

    # Prints items in the list.
    def print_list(self):
        current_node = self
        print("Linked List Contents:")
        if current_node is None:
            return
        while current_node is not None:
            print(current_node.item)
            current_node = current_node.next


# Returns a new root of a copied linked list.
def copy_linked_list(old_list):
    if old_list is None:
        print("This is a empty list!")
        return None

    current_node = old_list
    new_list = Node(None, None)
    temp_list = [None] * old_list.size()
    for i in range(old_list.size()):
        temp_list[i] = current_node.item
        current_node = current_node.next

    for j in range(old_list.size() - 1, -1, -1):
        new_list.add_node(temp_list[j])

    new_list = new_list.next
    return new_list


# Merges the two files into a linked list.
def merge_id_files(file_name1, file_name2):
    lines = [line.rstrip('\n') for line in open(file_name1)]
    id_list = Node(None, None)

    for i in range(len(lines)):
        # print(lines[i])
        id_list.add_node(int(lines[i]))

    lines2 = [line.rstrip('\n') for line in open(file_name2)]

    for i in range(len(lines2)):
        # print(lines2[i])
        id_list.add_node(int(lines2[i]))

    id_list = id_list.next

    return id_list


# Used for Solution's 2 and 3. After sorted, this prints out the duplicates and how many seen.
def count_duplicates(id_list):
    if id_list is None:
        print("This is a empty list!")
        return None

    current_node = id_list
    counter = 1
    while current_node.next is not None:
        id_check = current_node.item
        if current_node.item == current_node.next.item:
            counter = counter + 1
        elif counter > 1:
            print("ID #", id_check, " is seen ", counter, " times.")
            counter = 1
        current_node = current_node.next


# Solution 1 - Checks for duplicates using nested loop.
def check_id_duplicates(id_list):
    if id_list is None:
        print("This is a empty list!")
        return
    current_node1 = id_list
    current_node2 = id_list
    counter = 1
    seen_ids = [None] * id_list.size()  # Creates list to store numbers already seen so we can count them.
    for i in range(id_list.size() - 1):
        id_check = current_node1.item
        seen_ids[i] = id_check
        # print("id_check is ",id_check)
        for j in range(id_list.size() - 1):
            # print(id_check, " compared with ", current_node2.get_item())
            if id_check == seen_ids[j] and j != i:  # Checks to see if we have seen the number already.
                counter = -1
            elif id_check == current_node2.item and i < j:
                counter = counter + 1
                # print(id_check, " checked with", current_node2.get_item())
            current_node2 = current_node2.next
        if counter > 1:
            print("ID #", id_check, " is seen ", counter, " times.")
        counter = 1
        current_node2 = id_list.next
        current_node1 = current_node1.next


# Solution 2 - Sorts using Bubble Sort then checks for duplicates.
def bubble_sort_check(id_list):
    if id_list is None:
        print("This is a empty list!")
        return None

    if id_list.size() == 1:
        print("List size is 1. Does not need to be sorted")
        return
    switched = True  # Keeps track of weather there has been a swapping of data or not.
    while switched is True:
        current_node = id_list
        switched = False
        while current_node.next is not None:
            if current_node.item > current_node.next.item:
                # print(current_node.get_item(), " is greater than ", current_node.get_next().get_item())
                # print(current_node.get_item() - current_node.get_next().get_item())
                temp_item = current_node.item
                current_node.item = current_node.next.item
                current_node.next.item = temp_item
                switched = True
            current_node = current_node.next

    count_duplicates(id_list)
    return


# Solution 3 - Sorting using merge sort on linked list.
def merge_sort(id_list):
    if id_list is None:
        print("This is a empty list!")
        return None

    forward = id_list  # Stays in front to keep track of right split.
    behind = id_list  # Stays behind to create the split in the list.

    # Base Case - Once the linked list only has one node, it returns.
    if id_list.size() == 1:
        return id_list

    # Traverses linked list to find the split and right.
    for i in range(id_list.size() // 2):
        forward = forward.next
        if i < (id_list.size() // 2) - 1:
            behind = behind.next

    # Creates two headers, one for left side of list and the other for the right.
    behind.next = None
    left_head = id_list
    right_head = forward

    left_head = merge_sort(left_head)
    right_head = merge_sort(right_head)

    return merge(left_head, right_head)


# Goes through the separated linked list and orders them into one linked list.
def merge(left_node, right_node):
    temp_left_node = left_node
    temp_right_node = right_node
    sorted_list = Node(None, None)
    temp_list = sorted_list

    # Sorts the numbers into a linked list while they both are not empty.
    while temp_left_node is not None and temp_right_node is not None:
        if temp_left_node.item > temp_right_node.item:
            temp_list.next = Node(temp_right_node.item, None)
            temp_right_node = temp_right_node.next
            temp_list = temp_list.next
        else:
            temp_list.next = Node(temp_left_node.item, None)
            temp_left_node = temp_left_node.next
            temp_list = temp_list.next

    # Sorts the rest of the left sides nodes if there is still some remaining.
    while temp_left_node is not None:
        temp_list.next = Node(temp_left_node.item, None)
        temp_left_node = temp_left_node.next
        temp_list = temp_list.next

    # Sorts the rest of the right sides nodes if there is still some remaining.
    while temp_right_node is not None:
        temp_list.next = Node(temp_right_node.item, None)
        temp_right_node = temp_right_node.next
        temp_list = temp_list.next

    return sorted_list.next


# Solution 4 - Checks for duplicates using boolean array.
def boolean_array_check(id_list):
    if id_list is None:
        print("This is a empty list!")
        return None

    current_node = id_list
    seen = [False] * (6001)  # Boolean array with 1 size larger.
    for i in range(len(seen)):
        if seen[current_node.item] is True:
            print("Duplicate ID found in list.")
            return True
        else:
            seen[current_node.item] = True
        current_node = current_node.next

    print("No duplicate found.")
    return False


if __name__ == '__main__':
    main()




















































    # def get_item(self):
    #     return self.item
    #
    # def get_next(self):
    #     return self.next
    #
    # def set_item(self, new_item):
    #     self.item = new_item
    #
    # def set_next(self, next_node):
    #     self.next = next_node
    #

