import stripe
from github import Github, GithubException
from config import STRIPE_API_KEY, GITHUB_TOKEN, GITHUB_REPO_NAME, GITHUB_COMMIT_MESSAGE
import datetime

# Set up Stripe with the provided API key
stripe.api_key = STRIPE_API_KEY

# Set up GitHub with the provided token
g = Github(GITHUB_TOKEN)

def check_commit(repo_name, commit_message):
    try:
        # Get the specified repository
        repo = g.get_repo(repo_name)
        # Retrieve commits from the past day
        commits = repo.get_commits(since=datetime.datetime.now() - datetime.timedelta(days=1))
        print(f"Commits Found Today: {commits.totalCount}")

        # Check if there are no commits in the repository
        if commits.totalCount == 0:
            print("Repository has no commits.")
            return False

        # Check each commit for the specified message
        for commit in commits:
            if commit_message in commit.commit.message:
                return True

        # Return False if the commit message is not found
        return False

    # Handle exceptions from the GitHub API
    except GithubException as e:
        print(f"An error occurred: {e}")
        # Return False if an error occurs, but consider handling this differently
        return False

def create_test_charge():
    try:
        # Create a test charge with Stripe
        charge = stripe.Charge.create(
            amount=1000,  # amount in cents ($10.00)
            currency='usd',
            source='tok_visa',  # Use a test token
            description='Test charge from Git Goal Keeper'
        )
        print("Charge created:", charge)
    except stripe.error.StripeError as e:
        # Handle Stripe errors
        print("Error creating charge:", e)

if __name__ == "__main__":
    repo_name = GITHUB_REPO_NAME
    commit_message = GITHUB_COMMIT_MESSAGE

    # Check for the commit, create a charge if not found
    if check_commit(repo_name, commit_message):
        print("Bravo! GitHub Commit found. No charge created.")
    else:
        print("Uh ho! No GitHub commit found. Creating a charge via Stripe")
        create_test_charge()
