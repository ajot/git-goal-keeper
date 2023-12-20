# GitGoalKeeper

## What is GitGoalKeeper
GitGoalKeeper is a simple Python script designed to help developers stick to their daily coding goals. I created it to bring a bit of accountability and fun into my daily coding routine.

It works by automatically checking for commits in a specific GitHub repository each day (specified in `config.py`). If you don't make your daily commit, GitGoalKeeper steps in and logs a 'charge' in Stripe's test mode (by default).

For now, it's set up to make test logs of charges, which I'll review at the end of each week. Then, I plan to transfer an equivalent amount to a charity or cause of my choice.

## Who is it for?
This tool is ideal for individual developers, hobbyists, or anyone looking to add a bit of motivation to their daily coding routine.

## Getting Started

### Prerequisites
- Python 3.x
- Stripe account (in test mode)
- GitHub account
- Basic knowledge of Python and APIs

### Installation
1. **Clone the Repository**
   ```
   git clone https://github.com/your-repository-url.git
   cd your-project-directory
   ```

2. **Set Up a Virtual Environment (Optional)**
   ```
   python3 -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install Required Libraries**
   ```
   pip install -r requirements.txt
   ```

4. **API Keys and Configuration**
   - Rename `config-sample.py` to `config.py` in the project directory.
   - Add your Stripe secret key and GitHub token to the `config.py` file.
   - Ensure `config.py` is listed in `.gitignore`.

## Setting Up Stripe Keys and GitHub Tokens

### Stripe API Keys
For GitGoalKeeper, you will need to use your Stripe secret key. Remember, do not use the publishable key as it is meant for client-side operations.

1. **Obtain Secret Key from Stripe**:
   - Log in to your Stripe dashboard.
   - Navigate to the Developers section, then to API keys.
   - Copy the Secret Key (begins with `sk_live_` for live mode or `sk_test_` for test mode).

2. **Adding to GitGoalKeeper**:
   - In your `config.py`, replace the placeholder with your actual Stripe secret key.

### GitHub Personal Access Tokens
Personal Access Tokens (PATs) are required to authenticate your GitHub account in GitGoalKeeper.

1. **Creating a PAT on GitHub**:
   - Go to GitHub and log in.
   - Click on your profile picture, then select 'Settings'.
   - On the left sidebar, click 'Developer settings', then 'Personal access tokens'.
   - Click 'Generate new token', give it a name, and select the scopes or permissions you want to grant this token. For GitGoalKeeper, you'll need repo scope to access private repositories or public_repo for public ones.
   - Click 'Generate token' at the bottom of the page.

2. **Handling GitHub Tokens**:
   - Copy the generated token immediately, as GitHub won’t show it again.
   - In `config.py`, replace the GitHub token placeholder with your new token.

### Security Note:
- **Never share your secret keys or tokens**. Keep them confidential to maintain the security of your account.
- Ensure that `config.py` is included in your `.gitignore` file to prevent accidentally pushing it to a public repository.

4. **API Keys and Configuration**
   - Rename `config-sample.py` to `config.py` in the project directory.
   - Add your Stripe secret key and GitHub token to the `config.py` file.
   - Ensure `config.py` is listed in `.gitignore`.

### Usage
- Run `main.py` to start the tool.
- The script checks your GitHub for the specified commit each day.
- If the commit is not found, it logs a charge in Stripe.
- The console will display messages indicating whether a commit was found and if a charge was logged.

## Frequently Asked Questions (FAQs)

**Q: What is the difference between Stripe's secret and publishable keys?**  
**A:** The secret key (begins with `sk_test_`) is used for server-side operations like creating charges. The publishable key is for client-side operations and should not be used for charge creation.

**Q: Why am I getting a 'Repository is empty' error from GitHub?**  
**A:** This error occurs when the specified repository has no commits. Ensure that the repository has at least one commit.

**Q: How do I ensure the security of my API keys?**  
**A:** Store your API keys in a `config.py` file and add this file to `.gitignore`. Never hardcode sensitive keys directly in your scripts.

## TODO

- [ ] Integrate PayPal for automated financial transactions.
- [ ] Explore Venmo integration for manual transaction reminders.
- [ ] Implement additional financial consequences (e.g., donations, investments).
- [ ] Add more robust error handling and logging.