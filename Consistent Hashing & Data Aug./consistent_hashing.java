public class Solution {
    /*
     * @param n: a positive integer
     * @return: n x 3 matrix
     */
    private class Node {
        int start;
        int end;
        int id;
        Node(int start, int end, int id) {
            this.start = start;
            this.end = end;
            this.id = id;
        }
    }
    private class NodeHeapComparator implements Comparator<Node> {
        public int compare(Node a, Node b) {
            if ((b.end - b.start) == (a.end - a.start)) {
                return a.id - b.id;
            }
            return (b.end - b.start) - (a.end - a.start);
        }
    }
    public List<List<Integer>> consistentHashing(int n) {
        // write your code here
        List<List<Integer>> result = new ArrayList<>();
        if (n < 1) {
            return result;
        } else if (n == 1) {
            result.add(Arrays.asList(0, 359, 1));
            return result;
        }
        PriorityQueue<Node> maxHeap = new PriorityQueue(11, new NodeHeapComparator());
        maxHeap.offer(new Node(0, 359, 1));
        for (int i = 2; i <= n; i++) {
            Node node = maxHeap.poll();
            int mid = (node.start + node.end) / 2;
            maxHeap.offer(new Node(node.start, mid, node.id));
            maxHeap.offer(new Node(mid + 1, node.end, i));
        }
        while (!maxHeap.isEmpty()) {
            Node node = maxHeap.poll();
            result.add(Arrays.asList(node.start, node.end, node.id));
        }
        return result;
    }
}
// 对于每次新加的机器，需要寻找所有已知的机器中范围最大的那一个，进行切分。因此可以用Heap来加速寻找最大的过程。每次从Heap中返回最大的机器，切分完成后与新家的机器一起重新加入Heap，供下一次选取。

// Time Complexity: O(nlogn)
// Space Complexity: O(n)
// ref: https://www.jiuzhang.com/solution/consistent-hashing/#tag-other