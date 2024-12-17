# player_analysis_with_classes_refactored.py

# Step 1: Define a Player Class
class Player:
    # Define player attributes (name, points, assists, rebounds)
    def __init__(self, name, points, assists, rebounds):
        self.name = name
        self.points = points
        self.assists = assists
        self.rebounds = rebounds

    # method to calcualte averages
    def calculate_averages(self):
        # calculate the average points, assists, and rebounds
        avg_points = sum(self.points) / len(self.points)
        avg_assists = sum(self.assists) / len(self.assists)
        avg_rebounds = sum(self.rebounds) / len(self.rebounds)
        return avg_assists, avg_points, avg_rebounds

    # method to display the player's performance
    def display_player_performance(self):
        # properly formatted string using f-string to includes the player's name
        avg_points, avg_assists, avg_rebounds = self.calculate_averages()
        print(f"\n{self.name}'s Average Stats (Last 5 games):")
        print(f"Points: {avg_points:.2f}, Assists: {avg_assists:.2f}, Rebounds: {avg_rebounds:.2f}")

# Step 2: Define Supporting Functions

# Function to display a welcome message
def display_welcome():
    print('Welcome to the Fantasy Player Analysis and Projection Tool!')
    print("Here, you can enter a player's name to get their projected stats based on previous performance.")

# function to get player's name
def get_player_name():
    return input("\nEnter the name of the player you want to analyze (or type 'exit' to quit): ").title()

# Step 3 main function to run the program
def main():
    # display welcome message
    display_welcome()

    # Player Data (Using Player Objects)
    player_stats = {
        "Jared McCain": Player("Jared McCain", [15, 18, 30, 20, 20], [1, 0, 3, 5, 4], [6, 0, 5, 2, 4]),
        "Dalton Knecht": Player("Dalton Knecht", [20, 20, 7, 9, 17], [4, 1, 0, 1, 1], [6, 8, 4, 5, 4])
    }

    # loop to allow multiple analyses
    while True:
        # get player's name from user 
        player_name = get_player_name()

        # exit condition
        if player_name.lower() == "exit":
            print("\nThank you for using the Fantasy Player Analysis and Projection Tool. Goodbye!")
            break

        # Check if the player exisits and provide analysis
        if player_name in player_stats:
            player = player_stats[player_name]
            player.display_player_performance()
        else:
            # Handle case where player is not found
            print("\nPlayer not found. Please try again.")

# Step 4: Run the Program
if __name__ == "__main__":
    main()



