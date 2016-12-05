#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def length(self):
        """
        Return the length of this hash table by traversing its buckets
        Best case: Om(1) list is empty or only 1 element
        Worst case: O(n^m where m is the length of linked list in each bucket) list is not empty, check every item
        """
        # TODO: Count number of key-value entries in each of the buckets

        total_length = 0
        # iterate over all buckets, find length of buckets
        for bucket in self.buckets:
            total_length += bucket.length()
        return total_length

    def contains(self, key):
        """
        Return True if this hash table contains the given key, or False
        Best case: Om(1) hash table is empty
        Worst case: O(n) check entire linked list in bucket for key
        """
        # TODO: Check if the given key exists in a bucket

        # traverse linked list, find item via key, then return true or false if found
        chosen_bucket = self._bucket_index(key)
        linked_list_from_chosen_bucket = self.buckets[chosen_bucket]
        if_key_exists = linked_list_from_chosen_bucket.find(lambda data: key is data[0])
        if if_key_exists:
            return True
        else:
            return False

        # ternery version of above
        # return True if self.buckets[self._bucket_index(key)].find(lambda data: key is data[0]) is not None else False

    def get(self, key):
        """
        Return the value associated with the given key, or raise KeyError
        Best case: Om(1) hash table is empty
        Worst case: O(n) check entire linked list in specified bucket to find value
        """
        # TODO: Check if the given key exists and return its associated value

        # traverse linked list, find item via key, then return value
        chosen_bucket = self._bucket_index(key)
        linked_list_from_chosen_bucket = self.buckets[chosen_bucket]
        data_from_node_in_linked_list = linked_list_from_chosen_bucket.find(lambda data: key == data[0])  # key position in data array
        if data_from_node_in_linked_list is not None:
            return data_from_node_in_linked_list[1]
        else:
            raise KeyError

    def set(self, key, value):
        """
        Insert or update the given key with its associated value
        Best case: Om(1) hash table is empty
        Worst case: O(1) check entire linked list in specified bucket to find value
        """
        # TODO: Insert or update the given key-value entry into a bucket

        chosen_bucket = self._bucket_index(key)
        linked_list_from_chosen_bucket = self.buckets[chosen_bucket]
        data_from_node_in_linked_list = linked_list_from_chosen_bucket.find(lambda data: key == data[0])  # key position in data array
        if data_from_node_in_linked_list is None:
            # if not append to bucket as data array
            self.buckets[chosen_bucket].append([key, value])
        else:
            # if so, update value in data array
            data_from_node_in_linked_list[0] = key
            data_from_node_in_linked_list[1] = value

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # TODO: Find the given key and delete its entry if found
        chosen_bucket = self._bucket_index(key)
        linked_list_from_chosen_bucket = self.buckets[chosen_bucket]
        # if statement function mutates bucket while checking for ValueError to raise KeyError
        linked_list_from_chosen_bucket.deleteByKey(key)

    def keys(self):
        """Return a list of all keys in this hash table"""
        # TODO: Collect all keys in each of the buckets
        key_list = []
        for linked_list in self.buckets:
            # for each item in the linked list, append all available keys, which reside in array index 0
            linked_list.map(lambda data: key_list.append(data[0]))
        return key_list

    def values(self):
        """Return a list of all values in this hash table"""
        # TODO: Collect all values in each of the buckets
        value_list = []
        for linked_list in self.buckets:
            # for each item in the linked list, append all available keys, which reside in array index 1
            linked_list.map(lambda data: value_list.append(data[1]))
        return value_list
