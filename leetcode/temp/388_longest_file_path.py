# Suppose we represent our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

class Soultion(object):
    def longest_file_path(self, input):
        if not input:
            return 0
        dirs=input.split('\n')
        stack = list()
        curr_stack_length=0
        longest_file_path_length=0
        for d in dirs:
            tab_count=0
            while d[tab_count]=='\t':
                tab_count+=1

            while stack and stack[-1][0]>=tab_count:
                item=stack.pop(-1)
                curr_stack_length -=item[2]
            stack.append([tab_count, d[tab_count:],len(d)- tab_count])
            curr_stack_length+=stack[-1][2]
            if '.' in d and curr_stack_length + len(stack)-1 >longest_file_path_length:
                longest_file_path_length= curr_stack_length+ len(stack)-1
            # print stack, curr_stack_length
        return longest_file_path_length

if __name__=="__main__":
    obj= Soultion()
    string= "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print obj.longest_file_path(string)
