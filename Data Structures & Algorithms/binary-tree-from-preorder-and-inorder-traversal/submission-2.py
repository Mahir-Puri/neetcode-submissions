
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        # Store each value's index in the inorder array.
        inorder_map = {}

        for i, value in enumerate(inorder):
            inorder_map[value] = i

        # Tracks which preorder value to process next.
        self.preorder_index = 0

        def dfs(left, right):

            # No nodes exist in this subtree.
            if left > right:
                return None

            # Preorder always gives us the root first.
            root_value = preorder[self.preorder_index]

            # Move to the next preorder element.
            self.preorder_index += 1

            # Create the root node.
            root = TreeNode(root_value)

            # Find root position in inorder in O(1).
            mid = inorder_map[root_value]

            # Build the left subtree first.
            root.left = dfs(left, mid - 1)

            # Then build the right subtree.
            root.right = dfs(mid + 1, right)

            # Return the completed subtree.
            return root

        # Build the entire tree.
        return dfs(0, len(inorder) - 1)
