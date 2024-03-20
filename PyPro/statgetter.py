import requests
import matplotlib.pyplot as plt

# Replace with your CricAPI key
API_KEY = "37452636-7966-411a-b50d-5390cfd96380"

def fetch_team_stats(team_name):
    url = f"https://cricapi.com/api/matches?apikey={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status code is not 200
        data = response.json()
        team_matches = [match for match in data["matches"] if match["team-1"] == team_name or match["team-2"] == team_name]
        total_matches = len(team_matches)
        team_wins = sum(1 for match in team_matches if match["winner"] == team_name)

        print(f"{team_name} Stats:")
        print(f"Total Matches Played: {total_matches}")
        print(f"Total Wins: {team_wins}")

        # User input for chart type
        chart_type = input("Enter 'pie' for a pie chart, 'bar' for a bar chart, or 'both' for both: ")

        if chart_type.lower() in ['pie', 'both']:
            plt.figure(figsize=(8, 6))
            plt.pie([team_wins, total_matches - team_wins], labels=['Wins', 'Losses'], autopct='%1.1f%%', startangle=90)
            plt.title(f"{team_name} Win Percentage")
            plt.show()

        if chart_type.lower() in ['bar', 'both']:
            plt.figure(figsize=(8, 6))
            plt.bar(['Wins', 'Losses'], [team_wins, total_matches - team_wins], color=['green', 'red'])
            plt.xlabel("Outcome")
            plt.ylabel("Count")
            plt.title(f"{team_name} Match Outcomes")
            plt.show()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    league_name = "IPL"  # You can customize this
    team_name = input(f"Enter a team name ({league_name}): ")
    fetch_team_stats(team_name)
