Feature: Manage To-Do List

    Scenario: Add a task to the to-do list
        Given the to-do list is empty
        When the user adds a task "Buy groceries" with description "Buy milk and eggs"
        Then the to-do list should contain "Buy groceries"

    Scenario: List all tasks in the to-do list
        Given the to-do list contains tasks:
            | Task | Description |
            | Buy groceries | Buy milk and eggs |
            | Pay bills | Electricity and water |
        When the user lists all tasks
        Then the output should contain:
            """
            Buy groceries
            Pay bills
            """

    Scenario: Mark a task as completed
        Given the to-do list contains a task "Buy groceries" with description "Buy milk and eggs" and status "Pending"
        When the user marks the task "Buy groceries" as completed
        Then the task "Buy groceries" should have status "Completada"

    Scenario: Clear the entire to-do list
        Given the to-do list contains tasks:
            | Task |
            | Buy groceries |
            | Pay bills |
        When the user clears the to-do list
        Then the to-do list should be empty

    Scenario: Edit an existing task
        Given the to-do list contains a task "Buy groceries" with description "Buy milk" and status "Pending"
        When the user edits the task "Buy groceries" to have description "Buy milk and eggs"
        Then the task "Buy groceries" should have description "Buy milk and eggs"

    Scenario: View details of a specific task
        Given the to-do list contains a task "Pay bills" with description "Electricity and water" and status "Pending"
        When the user views the task "Pay bills"
        Then the output should contain:
            """
            Task: Pay bills
            Description: Electricity and water
            Status: Pending
            """