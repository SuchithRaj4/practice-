import java.util.*;

class TicketNode {
    String ticket;
    TicketNode next;

    public TicketNode(String ticket) {
        this.ticket = ticket;
        this.next = null;
    }
}

class TicketQueue {
    TicketNode front, rear;

    public TicketQueue() {
        this.front = this.rear = null;
    }

    public void enqueue(String ticket) {
        TicketNode newNode = new TicketNode(ticket);
        if (rear == null) {
            front = rear = newNode;
        } else {
            rear.next = newNode;
            rear = newNode;
        }
    }

    public void dequeue() {
        if (front == null) {
            System.out.println("Queue is empty.");
        } else {
            System.out.println("Processed Ticket: " + front.ticket);
            front = front.next;
            if (front == null) {
                rear = null;
            }
        }
    }

    public void display() {
        if (front == null) {
            System.out.println("Queue is empty.");
        } else {
            System.out.print("Current Queue: ");
            TicketNode temp = front;
            while (temp != null) {
                System.out.print(temp.ticket + " ");
                temp = temp.next;
            }
            System.out.println();
        }
    }
}

public class TicketingSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        TicketQueue queue = new TicketQueue();

        for (int i = 0; i < n; i++) {
            String input = sc.nextLine().trim();

            if (input.startsWith("ENQUEUE ")) {
                String ticket = input.substring(8).trim();
                queue.enqueue(ticket);
            } else if (input.equals("DEQUEUE")) {
                queue.dequeue();
            } else if (input.equals("DISPLAY")) {
                queue.display();
            } else {
                System.out.println("Invalid command.");
            }
        }
    }
}
