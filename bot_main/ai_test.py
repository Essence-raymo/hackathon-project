import json
import openai

# Load your API key from an environment variable or directly assign it here
openai.api_key = "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"

# Load the JSON data
def load_profiles():
    with open("hackathon-project/bot_main/database.json", "r") as f:
        return json.load(f)

# Prepare a prompt for GPT
def create_prompt(profiles):
    prompt = "You are an AI that creates teams based on user profiles. Here are the profiles:\n\n"
    
    for idx, profile in enumerate(profiles, start=1):
        prompt += f"Profile {idx}: {json.dumps(profile)}\n"
    
    prompt += (
        "\nPlease group these profiles into teams of 4 based on shared interests and complementary skills. "
        "Describe why you grouped them that way. Provide the output as a list of teams."
    )
    return prompt

# Send the prompt to GPT
def get_teams_from_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can also use "gpt-4" for more advanced results
        messages=[
            {"role": "system", "content": "You are an AI assistant specializing in team creation."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1000,
        temperature=0.7
    )
    
    tokens_used = response['usage']['total_tokens']
    print(f"Tokens used: {tokens_used}")
    return response['choices'][0]['message']['content']

# Main function to orchestrate the process
def create_teams(file_path):
    # Load profiles
    profiles = load_profiles()
    
    # Create a prompt
    prompt = create_prompt(profiles)
    
    # Get response from GPT
    teams = get_teams_from_gpt(prompt)
    
    return teams

# Run the script
if __name__ == "__main__":


    # Generate teams
    teams = create_teams("hackathon-project/bot_main/database.json")
    print("Generated Teams:\n", teams)
