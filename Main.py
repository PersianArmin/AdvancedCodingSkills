import json

class Menu:
    def display(self):
        pass

class MainMenu(Menu):
    def __init__(self, task_manager, expense_tracker, sudoku_game):
        self.task_manager = task_manager
        self.expense_tracker = expense_tracker
        self.sudoku_game = sudoku_game

    def display(self):
        while True:
            print("\nMain Menu:")
            print("1. Task Manager")
            print("2. Expense Tracker")
            print("3. Sudoku")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.task_manager.display()
            elif choice == '2':
                self.expense_tracker.display()
            elif choice == '3':
                self.sudoku_game.display()
            elif choice == '4':
                self.task_manager.save_data()
                self.expense_tracker.save_data()
                break
            else:
                print("Invalid choice. Please choose again.")

class TaskManager(Menu):
    def __init__(self, data_file='tasks.json'):
        self.tasks = []
        self.data_file = data_file
        self.load_data()

    def display(self):
        while True:
            print("\nTask Manager:")
            print("1. Add a task")
            print("2. Complete a task")
            print("3. Show all tasks")
            print("4. Back to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.complete_task()
            elif choice == '3':
                self.show_tasks()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please choose again.")

    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append({"task": task, "completed": False})
        print("Task added.")

    def complete_task(self):
        self.show_tasks()
        task_num = int(input("Enter the task number to complete: "))
        if 0 < task_num <= len(self.tasks):
            self.tasks[task_num - 1]["completed"] = True
            print("Task completed.")
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{idx + 1}. {task['task']} - {status}")

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.tasks, file)

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

class ExpenseTracker(Menu):
    def __init__(self, data_file='expenses.json'):
        self.expenses = []
        self.data_file = data_file
        self.load_data()

    def display(self):
        while True:
            print("\nExpense Tracker:")
            print("1. Add an expense")
            print("2. Edit an expense")
            print("3. Show a report")
            print("4. Back to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.edit_expense()
            elif choice == '3':
                self.show_report()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please choose again.")

    def add_expense(self):
        amount = float(input("Enter the amount: "))
        description = input("Enter the description: ")
        self.expenses.append({"amount": amount, "description": description})
        print("Expense added.")

    def edit_expense(self):
        self.show_expenses()
        exp_num = int(input("Enter the expense number to edit: "))
        if 0 < exp_num <= len(self.expenses):
            new_amount = float(input("Enter the new amount: "))
            new_description = input("Enter the new description: ")
            self.expenses[exp_num - 1] = {"amount": new_amount, "description": new_description}
            print("Expense edited.")
        else:
            print("Invalid expense number.")

    def show_expenses(self):
        if not self.expenses:
            print("No expenses.")
        else:
            for idx, exp in enumerate(self.expenses):
                print(f"{idx + 1}. ${exp['amount']} - {exp['description']}")

    def show_report(self):
        if not self.expenses:
            print("No expenses.")
        else:
            total = sum(exp['amount'] for exp in self.expenses)
            print(f"Total expenses: ${total:.2f}")
            self.show_expenses()

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.expenses, file)

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

class SudokuGame(Menu):
    def display(self):
        print("\nSudoku Game:")
        # Simple Sudoku game example.
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        self.print_board(board)
        while True:
            row = int(input("Enter row (0-8): "))
            col = int(input("Enter column (0-8): "))
            num = int(input("Enter number (1-9): "))

            if self.is_valid(board, row, col, num):
                board[row][col] = num
                self.print_board(board)

                if self.is_completed(board):
                    print("Congratulations! You completed the Sudoku.")
                    break
            else:
                print("Invalid move. Try again.")

    def print_board(self, board):
        for row in board:
            print(" ".join(str(num) if num != 0 else "." for num in row))

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def is_completed(self, board):
        for row in board:
            if 0 in row:
                return False
        return True

if __name__ == "__main__":
    task_manager = TaskManager()
    expense_tracker = ExpenseTracker()
    sudoku_game = SudokuGame()

    main_menu = MainMenu(task_manager, expense_tracker, sudoku_game)
    main_menu.display()

