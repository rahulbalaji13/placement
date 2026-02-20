Problem Statement



Create a base class called ItemDetails that has a method called getDetails(). This method contains details about the name, item number, and price.



Create a class DiscountedItem that is derived from the class ItemDetails. This class stores the discount percentage and the discounted price of the item. 



A customer purchases n items. Write a program to display the item-wise bill and total amount. The program should also display the total price of all items and the total discount amount.

Input format :
The first line of input consists of an integer n, representing the number of items.

The next inputs consist of the item name, item number, price, and discount percentage of n items in separate lines.

Output format :
The output displays item-wise details for each item in separate lines.

The following output displays the total price and the total discount amount of all the items in separate lines.



Refer to the sample output for the formatting specifications.

Code constraints :
In this scenario, the test cases fall under the following constraints:

1 <= n <= 20

1 <= Length of item name <= 20

1 <= item number <= 1000

1 <= price <= 1000

1 <= discount percentage <= 100

Sample test cases :
Input 1 :
2
Pen
012
120
2
Book
023
560
5
Output 1 :
Item-wise bill:
Item name: Pen
Item number: 12
Item price: 120
Discount percent: 2%
Discounted price: 117.6
Item name: Book
Item number: 23
Item price: 560
Discount percent: 5%
Discounted price: 532

Total price: 680
Total discount: 30.4


#include <iostream>
using namespace std;

class ItemDetails {
protected:
    string name;
    int itemNumber;
    float price;

public:
    void getDetails() {
        cin >> name;
        cin >> itemNumber;
        cin >> price;
    }

    float getPrice() {
        return price;
    }
};

class DiscountedItem : public ItemDetails {
public:
    float discountPercent;
    float discountedPrice;

    void calculateDiscountedPrice() {
        discountedPrice = getPrice() - (getPrice() * discountPercent / 100);
    }

    void displayDetails() {
        cout << "Item name: " << name << endl;
        cout << "Item number: " << itemNumber << endl;
        cout << "Item price: " << getPrice() << endl;
        cout << "Discount percent: " << discountPercent << "%" << endl;
        cout << "Discounted price: " << discountedPrice << endl;
    }
};

int main() {
    int n;
    float totalAmount = 0.0;
    float totalDiscount = 0.0;

    cin >> n;

    DiscountedItem items[n];

    for (int i = 0; i < n; i++) {
        items[i].getDetails();
        cin >> items[i].discountPercent;
        items[i].calculateDiscountedPrice();
    }

    cout << "Item-wise bill:" << endl;
    for (int i = 0; i < n; i++) {
        items[i].displayDetails();
        totalAmount += items[i].getPrice();
        totalDiscount += items[i].discountPercent / 100 * items[i].getPrice();
    }

    cout << endl << "Total price: " << totalAmount << endl;
    cout << "Total discount: " << totalDiscount << endl;

    return 0;
}


PROBLEM STATEMENT 2

Rosh is managing a smart circular queue-based parking system with exactly 10 parking spots, indexed from 0 to 9. When a car arrives, she parks it in the next available spot. If a car’s number is entered and the lot is full, she should be notified without consuming the car number. Cars leave the parking lot in the same order they arrived. Rosh also needs to handle cases when the lot is empty, and when an invalid operation code is entered.



Write a program to simulate this parking system with support for inserting and retrieving car numbers, full/empty conditions, and input validation.

Input format :
The first line contains an integer choice representing the operation type.

If choice == 1: Next line contains an integer carNumber to be parked.

If choice == 2: Retrieve the car at the front.

If choice == 3: Exit the program.

Any other value: Treated as an invalid choice.

Repeat until choice 3 is entered.

Output format :
For Insert operation (choice 1):

If parking is full, print "Parking lot is full."



Else: print "Car <carNumber> parked in spot <spotIndex>."

For Retrieve operation (choice 2):

If parking is empty: print "Parking lot is empty."

Else:

Print "Car <carNumber> retrieved from spot <spotIndex>."



For Exit operation (choice 3):

Program terminates without any output.



For any Invalid choice (not 1, 2, or 3): print "Invalid choice.



Refer to the sample output for the formatting specifications.

Code constraints :
Maximum number of parking spots: 10

1 ≤ carNumber ≤ 10000

Input operations continue until choice == 3 is encountered.

Sample test cases :
Input 1 :
1
123
1
456
2
3
Output 1 :
Car 123 parked in spot 0.
Car 456 parked in spot 1.
Car 123 retrieved from spot 0.
Input 2 :
2
3
Output 2 :
Parking lot is empty.
Input 3 :
1
153
1
156
5
3
Output 3 :
Car 153 parked in spot 0.
Car 156 parked in spot 1.
Invalid choice.
Input 4 :
1
131
1
132
1
133
1
134
1
135
1
136
1
137
1
138
1
139
1
140
1
3
Output 4 :
Car 131 parked in spot 0.
Car 132 parked in spot 1.
Car 133 parked in spot 2.
Car 134 parked in spot 3.
Car 135 parked in spot 4.
Car 136 parked in spot 5.
Car 137 parked in spot 6.
Car 138 parked in spot 7.
Car 139 parked in spot 8.
Car 140 parked in spot 9.
Parking lot is full.



# Define constants
MAX_SPOTS = 10

# Initialize variables
spots = [0] * MAX_SPOTS
front = -1
rear = -1

# Initialize the parking lot
def initialize():
    global front, rear
    front = rear = -1

# Check if the parking lot is full
def is_full():
    return (rear + 1) % MAX_SPOTS == front

# Check if the parking lot is empty
def is_empty():
    return front == -1

# Park a car
def park_car(car_number):
    global front, rear
    if is_full():
        print("Parking lot is full.")
    elif is_empty():
        front = rear = 0
        spots[rear] = car_number
        print(f"Car {car_number} parked in spot {rear}.")
    else:
        rear = (rear + 1) % MAX_SPOTS
        spots[rear] = car_number
        print(f"Car {car_number} parked in spot {rear}.")

# Retrieve a car
def retrieve_car():
    global front, rear
    if is_empty():
        print("Parking lot is empty.")
    elif front == rear:
        print(f"Car {spots[front]} retrieved from spot {front}.")
        initialize()  # Reset the parking lot when last car is retrieved
    else:
        print(f"Car {spots[front]} retrieved from spot {front}.")
        front = (front + 1) % MAX_SPOTS

def main():
    initialize()
    while True:
        try:
            choice = int(input())
            if choice == 1:
                if is_full():
                    print("Parking lot is full.")
                else:
                    car_number = int(input())
                    park_car(car_number)
            elif choice == 2:
                retrieve_car()
            elif choice == 3:
                break
            else:
                print("Invalid choice.")
        except EOFError:
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
