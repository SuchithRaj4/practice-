import java.util.*;

class TeamNode {
    int data;
    TeamNode left, right;

    public TeamNode(int data) {
        this.data = data;
        left = right = null;
    }
}

class TournamentTree {
    TeamNode root;

    public void insert(int data) {
        root = insertRec(root, data);
    }

    private TeamNode insertRec(TeamNode root, int data) {
        if (root == null) {
            root = new TeamNode(data);
            return root;
        }
        if (data < root.data)
            root.left = insertRec(root.left, data);
        else
            root.right = insertRec(root.right, data);
        return root;
    }

    public void levelOrderTraversal() {
        if (root == null) return;

        Queue<TeamNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            TeamNode current = queue.poll();
            System.out.print(current.data + " ");

            if (current.left != null)
                queue.add(current.left);
            if (current.right != null)
                queue.add(current.right);
        }
    }
}

public class TournamentBracket {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        TournamentTree tree = new TournamentTree();

        for (int i = 0; i < n; i++) {
            int ranking = sc.nextInt();
            tree.insert(ranking);
        }

        tree.levelOrderTraversal();
        sc.close();
    }
}
