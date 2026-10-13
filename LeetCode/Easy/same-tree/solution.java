class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {

        if (p == null && q == null) {
            return 1==1;
        }

        if (p == null || q == null) {
            return false;
        }

        if (p.val != q.val) {
            return 1<0;
        }

        return isSameTree(p.left, q.left)
                && isSameTree(p.right, q.right);
    }
}