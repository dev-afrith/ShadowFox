'''2. Imagine you are doing a workout routine, and you have to complete 100
jumping jacks.

Write a program that:
Asks you to perform 10 jumping jacks at a time.
After each set, it asks, "Are you tired?"

If you reply "yes" or "y," it should ask if you want to skip the remaining sets.
If you reply "yes" or "y," it should break and print, "You completed a total of
jumping jacks."

For example, if you did only 30 jumping jacks and answered "yes," the program
will break and print, "You completed a total of 30 jumping jacks."
If you reply "no" or "n," it should continue and display how many jumping jacks
are remaining. After that, ask you again, "Are you tired?"

For example, if you answered "no," it should display that 70 jumping jacks are
remaining and ask you again, "Are you tired?"
If you reply "no" or "n," it should continue and display how many jumping jacks
are remaining. After that, ask you again, "Are you tired?"

For example, if you answered "no," it should display that 70 jumping jacks are
remaining and ask you again, "Are you tired?"
If you complete all 100 jumping jacks, it should print, "Congratulations! You
completed the workout," and stop the program'''


total_jumping_jacks = 100
completed = 0

while completed < total_jumping_jacks:
    completed += 10
    print(f"\t\tYou have completed {completed} jumping jacks.\n")
    
    if completed >= total_jumping_jacks:
        print("Congratulations! You completed the workout.\n")
        break
    
    ask_tired = input("Are you tired? (type y for yes and n for no) : ").strip().lower()

    print("\n")
    if ask_tired == "y":
        next_set = input("Do you want to skip the remaining sets? (y for yes and n for no): ").strip().lower()
        if next_set == "y":
            print(f"\n\t\tYou completed a total of {completed} jumping jacks.\n")
            break
    elif ask_tired == "n":
        remaining_sets_to_complete = total_jumping_jacks - completed
        print(f"\t\tRemaining sets to complete = {remaining_sets_to_complete}\n")












    
        
