# Instagram Comment Scraper

This Python script uses the `instagrapi` library to log into an Instagram account, fetch the user ID of a specific account, and scrape the last 10 media posts along with their comments. The comments are then saved to individual JSON files.

## Features

- Logs into Instagram using environment variables for `USER_NAME` and `PASS_WORD`.
- Creates or loads a session to avoid re-authentication on subsequent runs.
- Fetches the last 10 media posts from a specified user account.
- Saves the comments of each post into separate JSON files.
- Appends new comments to existing files if they already exist.

## Requirements

- Python 3.x
- `instagrapi` library

## How it works

1. **Authentication**: The script uses `USER_NAME` and `PASS_WORD` from environment variables to log into Instagram. It attempts to load a session from a `session.json` file to avoid logging in every time.
   
2. **Fetching User Media**: The script fetches the last 10 media posts from the Instagram account `trainwithjoan`. You can change this username to another account by modifying the `username` parameter in the script.

3. **Saving Comments**: For each media post, it retrieves the comments and saves them to individual JSON files. If the file already exists, it appends new comments to the existing ones.

4. **Session Management**: If the session file is invalid or doesn't exist, the script will log in, create a new session, and save it to `session.json`.

5. **Rate Limiting**: The script waits for 2 minutes (`time.sleep(120)`) after scraping to avoid hitting rate limits.

## Notes

- Make sure to set your Instagram credentials (`USER_NAME` and `PASS_WORD`) as environment variables.
- Modify the script to scrape from a different user by changing the username in the `user_id_from_username` method.

## Example of Environment Variables

On Unix-based systems, you can set environment variables like this:

```bash
export USER_NAME="your_instagram_username"
export PASS_WORD="your_instagram_password"
